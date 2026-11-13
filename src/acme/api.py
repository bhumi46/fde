"""HTTP API for Acme's customer-service tool.

Run: uvicorn acme.api:app --reload   then open http://localhost:8000/docs
Phase 3 exercise: implement /shipments/late using `find_late_shipments` and `LateShipment`.
"""

from datetime import date

import pandas as pd
from fastapi import FastAPI, HTTPException

from acme.ingest import find_late_shipments, load_clean_shipments

app = FastAPI(title="Acme Shipments API", version="0.1.0")


def to_records(df: pd.DataFrame) -> list[dict]:
    """Convert a DataFrame to JSON-safe dicts (NaN/NaT become None)."""
    return df.astype(object).where(df.notna(), None).to_dict(orient="records")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/shipments")
def list_shipments(limit: int = 50) -> list[dict]:
    return to_records(load_clean_shipments().head(limit))


@app.get("/shipments/late")
def late_shipments(as_of: date | None = None) -> list[dict]:
    try:
        late = find_late_shipments(load_clean_shipments(), as_of or date.today())
    except NotImplementedError as exc:
        raise HTTPException(status_code=501, detail=str(exc)) from exc
    # TODO(phase 3): return validated LateShipment objects (add `days_late`) and
    #   support an optional `?carrier=` filter.
    return to_records(late)
