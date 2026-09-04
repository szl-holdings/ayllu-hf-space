# Terminal handoff — publish SZLHOLDINGS/ayllu

Canonical source is already fully coded Python:
https://github.com/szl-holdings/ayllu

The GitHub Action `.github/workflows/hf-space.yml` on that repo already uploads the folder to `SZLHOLDINGS/ayllu` when `HF_TOKEN` is present. If the token is missing it exits 0 and prints `HF_TOKEN UNAVAILABLE` — it does not fabricate LIVE.

## What Grok in terminal should do

1. Confirm Hub org `SZLHOLDINGS` and Space name `ayllu`.
2. If the Space does not exist, create it as Docker SDK, port 7860, Apache-2.0. If Hub rate-limits Space creation (20/day), wait — do not create a second product name.
3. Set Space secret `XAI_API_KEY` so Counsel / seats can answer LIVE with grok-4.5. Absent the secret, backend stays SOFTWARE.
4. From a checkout of `szl-holdings/ayllu`:

```bash
python -m pip install "huggingface_hub==1.19.0"
python - <<'PY'
from huggingface_hub import HfApi
import os
api = HfApi(token=os.environ["HF_TOKEN"])
api.upload_folder(
    folder_path=".",
    repo_id="SZLHOLDINGS/ayllu",
    repo_type="space",
    ignore_patterns=[".git*", "tests/*", ".venv/*", ".pytest_cache/*", "**/__pycache__/*", "**/*.pyc"],
)
print("published SZLHOLDINGS/ayllu")
PY
```

5. Smoke: `/`, `/counsel`, `/psyche`, `/health`, `/api/v1/ayllu/roster`, `/api/v1/ayllu/retrieve?q=lambda`, `/api/v1/ayllu/manifest`.
6. Do not claim the Space LIVE until the Hub page returns 200 and those paths answer.

## Do not

- Copy the council into a third repo and call that canonical.
- Train eleven models. Personas are roles on one routed backend.
- Admit the private 9464-node graph. Retrieve stays handles-only.
- Paint Λ green. Conjecture 1.
