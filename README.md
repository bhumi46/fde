# FDE Learning Lab: Acme Logistics engagement

A hands-on project for learning the **Forward Deployed Engineer** role.

## What an FDE does
An FDE is a software engineer embedded with a customer. Instead of building one product for everyone,
you work on site (or close to it) to make the product solve *this* customer's problem. The job mixes:

- **Discovery:** figure out the real problem behind the request.
- **Data integration:** connect to messy, real customer systems and data.
- **Building:** ship APIs, pipelines, AI features and small tools fast.
- **Deployment:** get it running in the customer's environment under their constraints.
- **Communication:** status updates, demos, handling expectations, handing over.

## The scenario
**Acme Logistics** keeps missing delivery promises and only finds out after the customer complains.
Their data is scattered across CSV and JSON exports and free-text driver notes. You are the FDE
assigned to them. Start with [`customer/brief.md`](customer/brief.md).

## How to use this repo
Work through the phases in order. Each guide has a goal, tasks, a deliverable and a "done when" check.

- [ ] [01 Discovery](phases/01-discovery.md): understand the problem, write the scope
- [ ] [02 Data integration](phases/02-data-integration.md): clean the shipment data (`src/acme/ingest.py`)
- [ ] [03 API](phases/03-api.md): expose late shipments over HTTP (`src/acme/api.py`)
- [ ] [04 AI feature](phases/04-ai-feature.md): summarize delay notes with Claude (`src/acme/summarize.py`)
- [ ] [05 Deploy](phases/05-deploy.md): containerize and configure
- [ ] [06 Handover](phases/06-handover.md): runbook, demo, final update

## Setup
```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -e '.[dev]'
pytest                         # some tests fail on purpose: they are your phase 2/3 exercises
uvicorn acme.api:app --reload  # http://localhost:8000/docs
```
For phase 4, copy `.env.example` to `.env` and set `ANTHROPIC_API_KEY`.

## Files for AI assistants
- [`AGENTS.md`](AGENTS.md): how AI agents should behave in this repo (commands, rules, boundaries).
- [`SKILLS.md`](SKILLS.md): step-by-step FDE playbooks for people and agents.
- `CLAUDE.md` points Claude Code at `AGENTS.md`.
