# Phase 3: API

**Goal:** Give Sam's customer-service tool an HTTP endpoint that lists late shipments.

## Tasks
1. Run the API: `uvicorn acme.api:app --reload`, open http://localhost:8000/docs, try `/health` and `/shipments`.
2. Finish the `TODO(phase 3)` in `src/acme/api.py`:
   - return `LateShipment` objects from `src/acme/models.py`, including `days_late`
   - add an optional `?carrier=` filter
3. Make `pytest tests/test_api.py` pass.
4. Write a usage example (`curl` command + sample response) for Sam's team.

## Concepts to learn
- FastAPI path/query parameters, response models, `TestClient`.
- Why the response shape is a contract: once Sam's tool parses it, renaming a field breaks production.
- Error design: 4xx for bad input with a helpful message, 5xx only for our bugs.

## Stretch
- Cache the cleaned data instead of re-reading the CSV on every request.
- Add `/carriers/scorecard`: on-time % per carrier.

## Done when
- [ ] All tests pass.
- [ ] `/docs` shows the endpoint with a clear description.
