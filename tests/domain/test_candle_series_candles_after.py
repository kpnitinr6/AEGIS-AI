"""
Tests for CandleSeries.candles_after().
"""

from datetime import datetime, timedelta, timezone
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
                5,
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


def test_returns_candles_after_reference() -> None:

    series = CandleSeries()

    first = make_candle(0)
    second = make_candle(5)
    third = make_candle(10)

    series.add(first)
    series.add(second)
    series.add(third)

    result = series.candles_after(second)

    assert result == [third]


def test_latest_returns_empty_list() -> None:

    series = CandleSeries()

    first = make_candle(0)
    second = make_candle(5)

    series.add(first)
    series.add(second)

    assert series.candles_after(second) == []


def test_unknown_candle_raises_value_error() -> None:

    series = CandleSeries()

    first = make_candle(0)

    series.add(first)

    unknown = Candle(
        instrument=Instrument(
            code="XAUUSD",
            name="Gold Spot",
        ),
        timeframe=Timeframe.M5,
        open_time=Time(
            datetime(
                2026,
                7,
                5,
                9,
                30,
                tzinfo=timezone.utc,
            )
        ),
        open=Decimal("3350"),
        high=Decimal("3360"),
        low=Decimal("3340"),
        close=Decimal("3355"),
        tick_volume=100,
    )

    with pytest.raises(ValueError):
        series.candles_after(unknown)