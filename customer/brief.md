# Customer brief: Acme Logistics

*Forwarded by the account executive after the kickoff call.*

> "We move about 2,000 shipments a week across the Midwest using four carriers. Our on-time rate is
> slipping and we usually find out a shipment is late when the customer calls us angry. We'd like an
> **API** our customer-service tool can call to see which shipments are late, and some kind of **AI
> summary** of why things are late. Our drivers leave notes but nobody has time to read them.
> We need something working in 6 weeks for the quarterly review."
> — Dana Ortiz, VP Operations

## What we were given
- `data/shipments.csv`: weekly export from their TMS (transport management system). "Mostly clean."
- `data/carriers.json`: carrier reference list from IT.
- `data/delay_notes.txt`: free-text notes drivers type into a mobile app.

## Known constraints (from the call)
- IT requires everything to run inside their AWS account; no customer data leaves it except to approved vendors.
- Customer-service tool can make HTTP GET calls and parse JSON. That's it.
- Two-person internal IT team will own whatever we build after handover.

## Things nobody has said yet
*(Your job in phase 1 is to find these out.)*
