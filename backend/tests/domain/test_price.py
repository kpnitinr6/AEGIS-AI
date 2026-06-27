from decimal import Decimal
from datetime import datetime, timezone

from backend.domain.instrument import Instrument
from backend.domain.price import Price
from backend.domain.time import Time


def test_price_creation():
    gold = Instrument(
        code="gold",
        name="Gold Spot",
    )

    market_time = Time(
        datetime(2026, 6, 27, 9, 15, tzinfo=timezone.utc)
    )

    price = Price(
        instrument=gold,
        amount=Decimal("3365.42"),
        time=market_time,
    )

    assert price.instrument == gold
    assert price.amount == Decimal("3365.42")
    assert price.time == market_time