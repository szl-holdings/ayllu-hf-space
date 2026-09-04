# PAYLOAD-01 — Hub occupancy closer

Operator kit. Not a flagship. Not KEEP-7.

## Destinations (locked)

| Layer | Where | Why |
|---|---|---|
| Source (this thread) | `szl-holdings/ayllu-hf-space` | Bind kit: TERMINAL_HANDOFF, OCCUPANCY, occupy script |
| Canonical council | `szl-holdings/ayllu` | Do not fork 11 seats into the bind repo |
| Hub runtime | existing `SZLHOLDINGS/ayllu` | `upload_folder` only. No `create_repo`. FOLD, not KEEP |
| Public walk | https://a11oy.net/ayllu/ | RECORD fold dest |
| Product bind | https://a-11-oy.com/ayllu | Already 200. Not a second Command Center |
| Desk | GET https://a-11-oy.com/spaces | KEEP-6 tiles only |
| RECORD | https://a11oy.net/spaces.json | contract 1.2.0 keep 6 / fold 38 |

## KEEP-6

`a11oy` · `killinchu` · `immune` · `szl-khipu` · `szl-atelier` · `governed-receipt-verifier`

Ayllu stays FOLD. Occupying Hub does not promote it.

## Run

```bash
pip install -q 'huggingface_hub==1.19.0'
export HF_TOKEN=hf_...
python3 scripts/payload01_hub_occupancy.py
```

If `HF_TOKEN` is missing the script MEASURES only and exits 0:
`HF_TOKEN UNAVAILABLE — Space publish skipped. Not fabricated LIVE.`

## Hard stops

- no DNS / grey-cloud / orange-cloud change
- no LIVE stamp (`receipt_minted` stays false)
- no rewrite of `a11oy.net/index.html`
- no `/verify` clone
- no Killinchu on proof front door
- no the-grid upload unless `package.json` + lockfile exist on `szl-holdings/the-grid` main
- no szl-forge#124 GPU
- Λ = Conjecture 1. energy 8/8 SIMULATED. occupancy UNAVAILABLE. locked-8 stays 8.

## Smoke (Hub)

`/` `/counsel` `/psyche` `/health` `/api/v1/ayllu/roster` `/api/v1/ayllu/manifest` `/api/v1/ayllu/retrieve?q=lambda`

Retrieve MEASURED 200 on 2026-09-04 (`/api/v1/ayllu/retrieve?q=lambda`). Bare `/retrieve?q=lambda` is 404. Backend stays SOFTWARE until `XAI_API_KEY` Space secret is set. Not LIVE.
