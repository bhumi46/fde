# Phase 4: AI feature

**Goal:** Turn the driver notes nobody reads into a summary of *why* shipments are late.

## Tasks
1. Confirm with Lee (IT) that sending notes to the Claude API is allowed. Record it in the decision log.
2. `cp .env.example .env`, add your `ANTHROPIC_API_KEY`, run `python -m acme.summarize`.
3. Follow **SKILLS.md → Adding an LLM feature safely**:
   - write 5 expected outputs by hand in `engagement/decision-log.md` (your eval set)
   - compare model output against them, then improve `SYSTEM_PROMPT`
4. Ask the model for structured output (JSON per shipment) so the API can return it.
5. Add `GET /shipments/{id}/delay-reason` that returns the summary for one shipment.
6. Write a unit test that passes a fake client, so tests never call the real API.

## Concepts to learn
- Prompting: role, task, format, and permission to say "unknown".
- Evals: you can't improve what you don't measure.
- Cost and latency: check `response.usage`; estimate cost for 2,000 shipments/week.
- Failure handling: refusals, rate limits, empty input, notes about shipments that don't exist (SH-1014).

## Done when
- [ ] Summary is correct on your eval set (you read every output).
- [ ] Endpoint works and has a test with a mocked client.
- [ ] Cost estimate is in your next status update.
