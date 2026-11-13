# Phase 2: Data integration

**Goal:** Turn the raw export into data you can trust, with tests proving it.

## Tasks
1. Profile the raw data (SKILLS.md → Messy-data triage, step 1):
   ```python
   from acme.ingest import load_raw_shipments
   df = load_raw_shipments(); df.info(); df["carrier"].value_counts(dropna=False)
   ```
2. Write an issues table in `engagement/discovery-notes.md`.
3. Run `pytest tests/test_ingest.py -v` and see which tests fail.
4. Finish the `TODO(phase 2)` items in `src/acme/ingest.py` one test at a time.
5. Log every judgment call in `engagement/decision-log.md` (date format, unknown carriers, `Lakeside` vs `Lakeside Haulers`).

## Concepts to learn
- `pd.to_datetime(..., format="mixed")` and why ambiguous dates are a *customer question*, not a code question.
- Deduplication: is a duplicate row an export bug or two real shipments? How would you find out?
- Mapping messy categories to a reference list (exact match, case/whitespace normalization, alias table).

## Done when
- [ ] All tests in `tests/test_ingest.py` pass.
- [ ] Decision log has at least 3 entries.
