# Terminal handoff — publish SZLHOLDINGS/ayllu

Canonical source is already fully coded Python:
https://github.com/szl-holdings/ayllu

The GitHub Action `.github/workflows/hf-space.yml` on that repo is the **single Hub writer** for `SZLHOLDINGS/ayllu`. It runs on push to `main` (or by dispatch), fails the run when `HF_TOKEN` is not configured (a missing credential is never a skip), commits from the exact main tip, waits for RUNNING at that commit, re-fetches every pushed byte and uploads an `hf-space-receipt` artifact only when the Hub commit and the runtime SHA match.

## What a terminal session should do

1. Do not create the Space, upload a folder or set Space secrets from a terminal. Those are owner actions; secret values are set by the owner and never copied into a session.
2. To publish, merge the change to `szl-holdings/ayllu` main (or dispatch its `hf-space` workflow) and read the run's `hf-space-receipt` artifact.
3. `XAI_API_KEY` (owner-set Space secret) is what lets Counsel / seats answer LIVE with the model pinned in code in `szl-holdings/ayllu` (`DEFAULT_GROK_MODEL`, Grok 4.7 / `grok-4.7`). Absent the secret, backend stays SOFTWARE.
   Do not set a model Space variable. `AYLLU_MODEL` is not read on the xAI path. `SZL_GROK_MODEL` (server-side only) is the owner's rollback lever: it accepts only the reviewed allowlist (`grok-4.7`, rollback `grok-4.5`); any other value fails closed with no xAI request (Counsel returns UNAVAILABLE, the seats stay SOFTWARE, no silent fallback). If it is set for a rollback, record who/when/why and delete it once the rollback is resolved.
4. `scripts/ayllu_occupy.py` in this bind repo is retired and refuses to run. It used to create the Space on any Hub error, upload the whole checkout and print MEASURED from HTTP 200 alone.

5. Smoke: `/`, `/counsel`, `/psyche`, `/health`, `/api/v1/ayllu/roster`, `/api/v1/ayllu/retrieve?q=lambda`, `/api/v1/ayllu/manifest`.
6. Do not claim the Space LIVE from HTTP 200 alone. Readback counts only when the workflow receipt shows the exact commit (hub_oid == created_oid == runtime.sha) and the smoke paths answer.

## Do not

- Copy the council into a third repo and call that canonical.
- Train eleven models. Personas are roles on one routed backend.
- Admit the private 9464-node graph. Retrieve stays handles-only.
- Paint Λ green. Conjecture 1.
