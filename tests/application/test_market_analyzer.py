"""
Tests for the MarketAnalyzer.
"""

from datetime import datetime, timezone
from decimal import Decimal

from backend.application.market_analyzer import MarketAnalyzer
from backend.domain import (
    Candle,
    Instrument,
    MarketContext,
    Time,
    Timeframe,
)


def make_instrument() -> Instrument:
    return Instrument(
        code="XAUUSD",
        name="Gold Spot",
    )


def make_candle() -> Candle:
    return Candle(
        instrument=make_instrument(),
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


def test_market_analyzer_returns_market_context() -> None:

    analyzer = MarketAnalyzer()

    context = analyzer.analyze(
        candles=[
            make_candle(),
        ]
    )

    assert isinstance(
        context,
        MarketContext,
    )

    assert (
        context.instrument.code
        == "XAUUSD"
    )

    assert (
        context.timeframe
        == Timeframe.M5
    )

    assert context.market_structure is None

    assert context.trend is None

    assert context.evidence == []