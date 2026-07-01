"""
Validation tests for the MarketAnalyzer.
"""

from datetime import datetime, timezone
from decimal import Decimal

import pytest

from backend.application.market_analyzer import MarketAnalyzer
from backend.domain import (
    Candle,
    CandleSeries,
    Instrument,
    Time,
    Timeframe,
)


def make_candle() -> Candle:
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
                1,
                9,
                0,
                tzinfo=timezone.utc,
            )
        ),
        open=Decimal("3300"),
        high=Decimal("3310"),
        low=Decimal("3290"),
        close=Decimal("3305"),
        tick_volume=100,
    )


def make_candle_series(count: int) -> CandleSeries:

    series = CandleSeries()

    for _ in range(count):
        series.add(make_candle())

    return series


def test_empty_candle_list_is_rejected() -> None:

    analyzer = MarketAnalyzer()

    with pytest.raises(ValueError):
        analyzer.analyze(
            make_candle_series(0),
        )


def test_single_candle_is_rejected() -> None:

    analyzer = MarketAnalyzer()

    with pytest.raises(ValueError):
        analyzer.analyze(
            make_candle_series(1),
        )


def test_two_candles_are_accepted() -> None:

    analyzer = MarketAnalyzer()

    context = analyzer.analyze(
        make_candle_series(2),
    )

    assert context is not None