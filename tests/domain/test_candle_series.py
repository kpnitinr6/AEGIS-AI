from datetime import datetime, timezone
from decimal import Decimal

import pytest

from backend.domain.candle import Candle
from backend.domain.candle_series import CandleSeries
from backend.domain.instrument import Instrument
from backend.domain.time import Time
from backend.domain.timeframe import Timeframe


def create_candle(close: str) -> Candle:
    return Candle(
        instrument=Instrument(
            code="gold",
            name="Gold Spot",
        ),
        timeframe=Timeframe.M5,
        open_time=Time(
            datetime(2026, 6, 27, 9, 15, tzinfo=timezone.utc)
        ),
        open=Decimal("3365.00"),
        high=Decimal("3368.00"),
        low=Decimal("3364.00"),
        close=Decimal(close),
        tick_volume=100,
    )


def test_add_and_latest():
    series = CandleSeries()

    candle = create_candle("3366.50")

    series.add(candle)

    assert series.latest() == candle


def test_previous():
    series = CandleSeries()

    first = create_candle("3365.00")
    second = create_candle("3366.00")

    series.add(first)
    series.add(second)

    assert series.previous() == first


def test_empty_series():
    series = CandleSeries()

    with pytest.raises(ValueError):
        series.latest()