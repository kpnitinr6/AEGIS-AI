"""
Tests for CandleSeries.
"""

from datetime import datetime, timezone
from decimal import Decimal

import pytest

from backend.domain import (
    Candle,
    CandleSeries,
    Instrument,
    Time,
    Timeframe,
)


def make_candle(
    *,
    minute: int,
) -> Candle:

    return Candle(
        instrument=Instrument(
            code="XAUUSD",
            name="Gold Spot",
        ),
        timeframe=Timeframe.M5,
        open_time=Time(
            datetime(
                2026,
                7,
                7,
                9,
                minute,
                tzinfo=timezone.utc,
            )
        ),
        open=Decimal("3350"),
        high=Decimal("3360"),
        low=Decimal("3340"),
        close=Decimal("3355"),
        tick_volume=100,
    )


def test_previous_of_returns_previous_candle() -> None:

    series = CandleSeries()

    candle1 = make_candle(minute=0)
    candle2 = make_candle(minute=5)
    candle3 = make_candle(minute=10)

    series.add(candle1)
    series.add(candle2)
    series.add(candle3)

    assert series.previous_of(candle3) == candle2


def test_previous_of_first_candle_returns_none() -> None:

    series = CandleSeries()

    candle = make_candle(minute=0)

    series.add(candle)

    assert series.previous_of(candle) is None


def test_previous_of_unknown_candle_raises() -> None:

    series = CandleSeries()

    known = make_candle(minute=0)
    unknown = make_candle(minute=5)

    series.add(known)

    with pytest.raises(ValueError):
        series.previous_of(unknown)