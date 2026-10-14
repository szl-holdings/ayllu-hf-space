#!/usr/bin/env python3
"""RETIRED legacy publisher for SZLHOLDINGS/ayllu. It refuses to run.

The single Hub writer for the Space SZLHOLDINGS/ayllu is the CI workflow
`.github/workflows/hf-space.yml` in szl-holdings/ayllu. That workflow fails
closed without its credential, commits from the exact main tip, waits for
RUNNING at that commit, re-fetches every pushed byte and records a receipt
only when hub_oid == created_oid and runtime.sha == created_oid.

This script used to create the Space on any Hub HTTP error (including 401,
403 and 429), upload the whole checkout with a short deny list, optionally
set a Space secret, and print "OCCUPANCY MEASURED" from HTTP 200 smoke paths
alone, with no exact-revision or source-byte check. It now does none of
that: it imports no Hub client, reads no token, makes no network request and
exits non-zero. Publish by merging to szl-holdings/ayllu main (or dispatching
its hf-space workflow), never from a local checkout.
"""
from __future__ import annotations

import sys

CANONICAL_WRITER = (
    "https://github.com/szl-holdings/ayllu/blob/main/.github/workflows/hf-space.yml"
)
EXIT_RETIRED = 64

MESSAGE = f"""\
RETIRED: scripts/ayllu_occupy.py no longer publishes SZLHOLDINGS/ayllu.
Nothing was created, uploaded, configured or measured. State: UNVERIFIED.
The single Hub writer for SZLHOLDINGS/ayllu is the CI workflow
  {CANONICAL_WRITER}
Publish by merging to szl-holdings/ayllu main or dispatching that workflow.
Readback evidence is its hf-space-receipt artifact (exact commit match), not
HTTP 200 smoke paths."""


def main(argv: list[str] | None = None) -> int:
    print(MESSAGE, file=sys.stderr)
    return EXIT_RETIRED


if __name__ == "__main__":
    raise SystemExit(main())
