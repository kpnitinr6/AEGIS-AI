from datetime import datetime, timezone
from decimal import Decimal

from backend.domain.candle import Candle
from backend.domain.instrument import Instrument
from backend.domain.time import Time
from backend.domain.timeframe import Timeframe


def test_candle_creation():
    gold = Instrument(
        code="gold",
        name="Gold Spot",
    )

    candle = Candle(
        instrument=gold,
        timeframe=Timeframe.M5,
        open_time=Time(
            datetime(2026, 6, 27, 9, 15, tzinfo=timezone.utc)
        ),
        open=Decimal("3365.10"),
        high=Decimal("3367.80"),
        low=Decimal("3364.90"),
        close=Decimal("3366.50"),
        tick_volume=1523,
    )

    assert candle.instrument == gold
    assert candle.timeframe == Timeframe.M5
    assert candle.close == Decimal("3366.50")