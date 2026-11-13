"""Tests that define "clean data". Phase 2 is done when all of these pass."""

from datetime import date

import pandas as pd

from acme.ingest import (
    clean_shipments,
    find_late_shipments,
    load_carriers,
    load_raw_shipments,
)


def clean() -> pd.DataFrame:
    return clean_shipments(load_raw_shipments())


# --- Passing from day one -------------------------------------------------

def test_raw_export_loads():
    assert "shipment_id" in load_raw_shipments().columns


def test_blank_rows_removed():
    assert clean()["shipment_id"].notna().all()


# --- Phase 2 exercises (fail until you finish ingest.py) ------------------

def test_no_duplicate_shipments():
    df = clean()
    assert df["shipment_id"].is_unique
    assert len(df) == 15


def test_dates_are_parsed():
    df = clean()
    for col in ["ship_date", "promised_date", "delivered_date"]:
        assert pd.api.types.is_datetime64_any_dtype(df[col]), col
    row = df.set_index("shipment_id").loc["SH-1003"]
    assert row["ship_date"].date() == date(2026, 10, 2)


def test_carriers_normalized():
    known = {c["name"] for c in load_carriers()} | {"UNKNOWN"}
    df = clean()
    assert set(df["carrier"]) <= known
    assert df.set_index("shipment_id").loc["SH-1006", "carrier"] == "FastFreight"


def test_status_lowercase():
    assert set(clean()["status"]) == {"delivered", "in_transit"}


def test_late_shipments():
    late = find_late_shipments(clean(), as_of=date(2026, 10, 10))
    assert set(late["shipment_id"]) == {
        "SH-1002", "SH-1004", "SH-1008", "SH-1011", "SH-1014",  # delivered late
        "SH-1005", "SH-1009", "SH-1013",                        # still in transit, overdue
    }
