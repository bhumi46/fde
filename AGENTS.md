# AGENTS.md

Instructions for AI coding agents (Claude Code, Codex, Cursor, Copilot, ...) working in this repo.

## What this repo is
A **learning project** for the Forward Deployed Engineer (FDE) role. The learner works a simulated
customer engagement with a fictional customer, **Acme Logistics**, phase by phase (`phases/01-*.md` → `06-*.md`).

## How to help: teach, don't just solve
- Code marked `TODO(phase N)` is the learner's exercise. **Do not fill it in unless explicitly asked.**
  Give hints, point to the relevant file/test, explain trade-offs, ask a guiding question.
- When the learner asks for a full solution, write it, then explain *why* it works and what an FDE would check next.
- Frame answers the way a customer engagement works: what does the customer need, what's the risk, how do we verify?
- For repeatable workflows (discovery, data triage, status updates, ...) follow the playbooks in [SKILLS.md](SKILLS.md).

## Setup and commands
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e '.[dev]'

pytest                          # run tests (some fail on purpose until TODOs are done)
pytest tests/test_ingest.py -v  # one file
ruff check .                    # lint
uvicorn acme.api:app --reload   # run the API on http://localhost:8000 (docs at /docs)
python -m acme.summarize        # LLM summary of delay notes (needs ANTHROPIC_API_KEY)
```

## Project map
| Path | Purpose |
|---|---|
| `customer/` | The "customer's world": brief, stakeholders, raw data. Read-only. |
| `phases/` | Learning guides, one per engagement phase. |
| `engagement/` | Learner's deliverables: discovery notes, scope, decision log, status updates. |
| `src/acme/` | Python package: `ingest.py` (data cleaning), `models.py`, `api.py` (FastAPI), `summarize.py` (Claude API). |
| `tests/` | pytest suite. Tests define "done" for each phase. |

## Conventions
- Python 3.11+, type hints on public functions, pydantic for data shapes.
- Small, pure functions in `ingest.py`; the API layer stays thin.
- Every behaviour change comes with a test.
- Prefer clear code over clever code: the customer's team will maintain it after handover.

## Boundaries
- **Never modify `customer/data/`.** It is the customer's source of truth; fix problems in code, not in the data.
- Never commit secrets. API keys go in `.env` (git-ignored); `.env.example` documents the variables.
- Record notable technical decisions in `engagement/decision-log.md` (what, why, alternatives).
- Don't add heavy dependencies without noting why in the decision log.

## Definition of done for a change
1. `pytest` passes for the tests of the current phase.
2. `ruff check .` is clean.
3. If behaviour visible to the customer changed, the relevant `engagement/` doc is updated.
