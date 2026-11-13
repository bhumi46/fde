"""Response shapes for the API. The customer-service tool depends on these field names."""

from datetime import date

from pydantic import BaseModel


class Shipment(BaseModel):
    shipment_id: str
    origin: str
    destination: str
    carrier: str
    ship_date: date | None
    promised_date: date | None
    delivered_date: date | None
    status: str


class LateShipment(Shipment):
    days_late: int
