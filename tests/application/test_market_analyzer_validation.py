"""
Tests for MarketAnalyzer validation.
"""

from datetime import datetime, timezone
from decimal import Decimal

import pytest

from backend.application.market_analyzer import MarketAnalyzer
from backend.domain import (
    Candle,
    Instrument,
    Time,
    Timeframe,
)


def make_candle() -> Candle:

    instrument = Instrument(
        code="XAUUSD",
        name="Gold Spot",
    )

    return Candle(
        instrument=instrument,
        timeframe=Timeframe.M5,
        open_time=Time(
            datetime(
                2026,
                7,
                1,
                tzinfo=timezone.utc,
            )
        ),
        open=Decimal("3300"),
        high=Decimal("3310"),
        low=Decimal("3290"),
        close=Decimal("3305"),
        tick_volume=100,
    )


def test_empty_candle_list_is_rejected() -> None:

    analyzer = MarketAnalyzer()

    with pytest.raises(ValueError):

        analyzer.analyze([])


def test_single_candle_is_rejected() -> None:

    analyzer = MarketAnalyzer()

    with pytest.raises(ValueError):

        analyzer.analyze(
            [
                make_candle(),
            ]
        )


def test_two_candles_are_accepted() -> None:

    analyzer = MarketAnalyzer()

    context = analyzer.analyze(
        [
            make_candle(),
            make_candle(),
        ]
    )

    assert context.instrument.code == "XAUUSD"