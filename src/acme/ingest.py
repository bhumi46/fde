"""Load and clean Acme's shipment exports.

Phase 2 exercise: finish the TODOs in `clean_shipments` and `find_late_shipments`
until `pytest tests/test_ingest.py` passes. Follow SKILLS.md -> "Messy-data triage".
"""

import json
from datetime import date
from pathlib import Path

import pandas as pd

DATA_DIR = Path(__file__).resolve().parents[2] / "customer" / "data"
DATE_COLUMNS = ["ship_date", "promised_date", "delivered_date"]


def load_raw_shipments(path: Path = DATA_DIR / "shipments.csv") -> pd.DataFrame:
    """Read the TMS export exactly as delivered, with no cleaning."""
    return pd.read_csv(path, dtype=str)


def load_carriers(path: Path = DATA_DIR / "carriers.json") -> list[dict]:
    """Read the carrier reference list from IT."""
    return json.loads(path.read_text())


def clean_shipments(df: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned copy of the raw shipments table."""
    df = df.dropna(how="all").copy()

    # TODO(phase 2): remove duplicate shipments (same shipment_id appears more than once).
    # TODO(phase 2): parse DATE_COLUMNS into datetimes. The export mixes 2026-10-01,
    #   10/02/2026 and "3 Oct 2026". Is 10/02 Oct 2 or Feb 10? Record your answer in
    #   engagement/decision-log.md.
    # TODO(phase 2): normalize `carrier` to the canonical names in carriers.json
    #   ("fast freight", "FASTFREIGHT " -> "FastFreight"). Anything unmatched -> "UNKNOWN".
    # TODO(phase 2): lowercase `status`.

    return df.reset_index(drop=True)


def find_late_shipments(df: pd.DataFrame, as_of: date) -> pd.DataFrame:
    """Return shipments that are late as of `as_of`.

    Late means: delivered after the promised date, OR not delivered yet and the
    promised date is before `as_of`. Expects the output of `clean_shipments`.
    """
    # TODO(phase 2): implement. Hint: build two boolean masks and combine with `|`.
    raise NotImplementedError("find_late_shipments is a phase 2 exercise")


def load_clean_shipments() -> pd.DataFrame:
    return clean_shipments(load_raw_shipments())
