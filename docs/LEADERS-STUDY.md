# Domain Leader Study — ayllu-hf-space (space bind / liveness ops)

OUROBOROS phase-3, cohort-01 tranche-2. PROPOSE-ONLY study card: documentation only, no production change in this PR.

## Domain leaders studied
| Leader | What they have | Key sources |
| --- | --- | --- |
| Docker HEALTHCHECK production patterns | Health checks distinct from readiness; exit-code contract; avoid health checks that always pass | oneuptime.com guide; hugow.dev notes |
| HF Spaces ops practice | Observability stacks (e.g. Phoenix tracing) deployed on Spaces; /health endpoint + external probe pattern | huggingface.co/learn/cookbook phoenix_observability_on_hf_spaces |
| L-MAD (ayllu lineage, cited in ayllu#80) | Manager-agent design lineage for this space's parent project | arXiv:2607.09099 (via ayllu leader study) |

## What the leaders do better
- Health is a measured contract: leaders define exactly which failures flip the check exit code, so a dead space is detected in seconds, not at next user visit.
- External probing: the checker lives outside the monitored process (UptimeRobot-style), so a wedged app cannot lie about its own health — matches our two-hands doctrine.
- Observability is separated from the app: tracing/metrics sidecars on Spaces keep app code clean and evidence post-mortemable.

## Absorb actions (proposed, NOT implemented in this PR)
- [ ] Define a /healthcheck route in the space whose exit contract is: dependencies live + bind token verified, else 5xx (no always-green).
- [ ] Document an external probe cadence (60s) with heartbeat receipts written to the estate ledger, fail-closed when a probe fails twice.
- [ ] Add a liveness section to the space README: what is measured, where heartbeats land, who alerts.
- [ ] Pin the space's runtime deps and record the digest in README so bind reproducibility is receipt-able.

## Sources
- Docker HEALTHCHECK patterns: https://oneuptime.com/blog/post/2026-01-06-docker-health-checks/view
- Phoenix on HF Spaces: https://huggingface.co/learn/cookbook/phoenix_observability_on_hf_spaces
