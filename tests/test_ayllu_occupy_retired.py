"""The retired legacy publisher must never touch the Hub. No network, no tokens."""
from __future__ import annotations

import contextlib
import importlib.util
import io
import socket
import sys
import types
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "ayllu_occupy.py"
DUMMY = "dummy-not-a-token"


class _HubError(Exception):
    def __init__(self, status: int):
        super().__init__(f"HTTP {status}")
        self.response = types.SimpleNamespace(status_code=status)


def _fake_hub():
    """A stand-in huggingface_hub whose every HfApi call is recorded and raises."""
    calls: list[str] = []

    class FakeApi:
        def __init__(self, *a, **k):
            calls.append("HfApi()")

        def __getattr__(self, name):
            def _call(*a, **k):
                calls.append(name)
                raise _HubError(403)

            return _call

    hub = types.ModuleType("huggingface_hub")
    hub.HfApi = FakeApi
    utils = types.ModuleType("huggingface_hub.utils")
    utils.HfHubHTTPError = _HubError
    hub.utils = utils
    return hub, utils, calls


def _load():
    spec = importlib.util.spec_from_file_location("ayllu_occupy_under_test", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _no_network(*a, **k):
    raise AssertionError("network access attempted")


class RetiredPublisherTest(unittest.TestCase):
    def _run(self, env: dict[str, str]):
        hub, utils, calls = _fake_hub()
        err, out = io.StringIO(), io.StringIO()
        with mock.patch.dict(
            sys.modules, {"huggingface_hub": hub, "huggingface_hub.utils": utils}
        ), mock.patch.dict("os.environ", env, clear=False), mock.patch(
            "urllib.request.urlopen", _no_network
        ), mock.patch.object(
            socket, "create_connection", _no_network
        ), contextlib.redirect_stderr(err), contextlib.redirect_stdout(out):
            mod = _load()
            code = mod.main([])
        return mod, code, out.getvalue() + err.getvalue(), calls

    def test_refuses_with_token_and_secret_present(self):
        mod, code, text, calls = self._run({"HF_TOKEN": DUMMY, "XAI_API_KEY": DUMMY})
        self.assertNotEqual(code, 0)
        self.assertEqual(code, mod.EXIT_RETIRED)
        self.assertEqual(calls, [], "no Hub client may be constructed or called")
        self.assertIn("RETIRED", text)
        self.assertIn(mod.CANONICAL_WRITER, text)
        self.assertNotIn(DUMMY, text, "token/secret values must never be echoed")

    def test_refuses_without_token(self):
        _, code, _, calls = self._run({"HF_TOKEN": "", "XAI_API_KEY": ""})
        self.assertNotEqual(code, 0)
        self.assertEqual(calls, [])

    def test_auth_and_rate_limit_errors_never_cause_create_or_upload(self):
        for status in (401, 403, 404, 429):
            with self.subTest(status=status):
                _, code, _, calls = self._run({"HF_TOKEN": DUMMY})
                self.assertNotEqual(code, 0)
                for forbidden in ("create_repo", "upload_folder", "upload_file",
                                  "create_commit", "add_space_secret"):
                    self.assertNotIn(forbidden, calls)

    def test_never_claims_measured_or_live(self):
        _, _, text, _ = self._run({"HF_TOKEN": DUMMY})
        self.assertNotIn("MEASURED", text)
        self.assertNotIn("LIVE", text.replace("Not fabricated LIVE", ""))
        self.assertIn("UNVERIFIED", text)

    def test_source_has_no_hub_write_or_upload_path(self):
        src = SCRIPT.read_text(encoding="utf-8")
        code_lines = [ln for ln in src.splitlines() if not ln.lstrip().startswith("#")]
        body = "\n".join(code_lines).split('"""', 2)[-1]  # drop module docstring
        for needle in ("import huggingface_hub", "from huggingface_hub", "HfApi(",
                       "create_repo(", "upload_folder(", "add_space_secret(",
                       "urlopen(", "os.environ"):
            self.assertNotIn(needle, body)


if __name__ == "__main__":
    unittest.main()
