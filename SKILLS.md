# SKILLS.md

Repeatable FDE playbooks. Each skill says **when** to use it, the **steps**, and the **output**.
Humans and AI agents both follow these. (To turn one into a native Claude Code skill, copy it into
`.claude/skills/<name>/SKILL.md` with `name` and `description` frontmatter.)

---

## 1. Customer discovery
**When:** Start of an engagement, or whenever the problem feels fuzzy.

**Steps**
1. Read `customer/brief.md` and `customer/stakeholders.md`. Note each stakeholder's goal and fear.
2. Separate **stated problem** ("we need an API") from **underlying problem** ("ops finds out about late shipments too late").
3. Draft questions in four buckets:
   - *Outcome:* What decision will this help you make? How do you measure success today?
   - *Workflow:* Walk me through the last time a shipment was late. Who noticed, and when?
   - *Data:* Where does the data live, who owns it, how fresh is it, what's known to be wrong?
   - *Constraints:* Security/IT rules, hosting, budget, deadline, who maintains it after we leave?
4. Write down assumptions you are making and mark which ones need validation.

**Output:** `engagement/discovery-notes.md` (questions, answers/assumptions) and a one-page `engagement/scope.md`
(problem, success metric, in scope, out of scope, risks).

---

## 2. Messy-data triage
**When:** Receiving any customer data export.

**Steps**
1. **Profile** before cleaning: row count, columns, dtypes, null counts, unique values per categorical column, date formats.
   ```python
   df.shape; df.dtypes; df.isna().sum(); df["carrier"].value_counts(dropna=False)
   ```
2. **List issues** as a table: issue, example, rows affected, proposed rule, question for customer.
3. **Write a test first** for each cleaning rule (`tests/test_ingest.py`), then implement it.
4. Never silently drop data: count what was removed and why, and log it.
5. Confirm ambiguous rules with the customer (e.g. "is `10/02/2026` Oct 2 or Feb 10?") and record the answer in the decision log.

**Output:** Cleaning functions + tests, and a data-quality section in `engagement/discovery-notes.md`.

---

## 3. Building an integration API
**When:** The customer needs other systems or people to consume the data.

**Steps**
1. Start from the consumer: who calls it, how often, what fields do they need?
2. Define the response shape with a pydantic model (`src/acme/models.py`).
3. Keep endpoints thin: load → transform (pure functions) → return.
4. Add `/health` first; add filters (`?carrier=`, `?limit=`) only when a consumer needs them.
5. Test each endpoint with FastAPI's `TestClient`; check `/docs` renders.
6. Return clear errors (4xx with a message), never a stack trace.

**Output:** Working endpoint, tests, and a short usage example in the README or runbook.

---

## 4. Adding an LLM feature safely
**When:** The customer has unstructured text (notes, emails, tickets) that people summarize by hand.

**Steps**
1. Write down the job: input, desired output format, who reads it, cost of a wrong answer.
2. Build a small eval set first: 5–10 real inputs with what a good output looks like.
3. Write the prompt: role, task, output format, "say 'unknown' if the notes don't say".
4. Call the model through the official SDK (`anthropic`), key from the environment, never hard-coded.
5. Handle failure modes: API errors, refusals (`stop_reason == "refusal"`), empty input, very long input.
6. Run the eval set, read every output, iterate. Note latency and token cost per call.
7. Keep a human in the loop for anything customer-facing until the eval results earn trust.

**Output:** `src/acme/summarize.py` feature, eval notes in the decision log, cost estimate in the status update.

---

## 5. Customer status update
**When:** Weekly, or after any milestone or blocker.

**Template**
```
Subject: Acme × FDE — week N update
TL;DR: one sentence (on track / at risk / blocked).
Done this week: 2–4 bullets, framed as customer outcomes.
Next week: 2–4 bullets.
Risks / asks: what we need from you, by when, and the impact if we don't get it.
Metrics: the success metric from scope.md, current value.
```
**Rules:** lead with the outcome, no jargon, one clear ask per update, bad news early.

**Output:** Append to `engagement/status-updates.md`.

---

## 6. Handover runbook
**When:** Final phase, before the customer's team takes ownership.

**Sections**
1. What it does (2 sentences) and architecture sketch.
2. How to run it locally and in production (exact commands).
3. Configuration and secrets (names, not values).
4. Common failures and how to fix them (bad data file, API key expired, LLM refusal).
5. How to change things safely (where the cleaning rules live, how to run tests).
6. Owners and escalation contacts.

**Output:** `engagement/runbook.md` + a 10-minute demo script.
