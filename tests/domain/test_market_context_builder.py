"""
Tests for the MarketContextBuilder.
"""

from datetime import datetime, timezone
from decimal import Decimal

from backend.domain import (
    Candle,
    Instrument,
    MarketStructure,
    MarketContext,
    StructurePoint,
    StructureType,
    Swing,
    SwingType,
    Time,
    Timeframe,
    Trend,
    TrendState,
)
from backend.understanding import MarketContextBuilder


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
                2,
                9,
                0,
                tzinfo=timezone.utc,
            )
        ),
        open=Decimal("3350"),
        high=Decimal("3360"),
        low=Decimal("3340"),
        close=Decimal("3355"),
        tick_volume=100,
    )


def make_market_structure() -> MarketStructure:
    structure = MarketStructure(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
    )

    structure.append(
        StructurePoint(
            structure=StructureType.HIGHER_HIGH,
            swing=Swing(
                candle=make_candle(),
                type=SwingType.HIGH,
            ),
        )
    )

    return structure


def make_trend() -> Trend:
    structure = make_market_structure()

    return Trend(
        state=TrendState.BULLISH,
        market_structure=structure,
    )


def test_build_market_context() -> None:

    builder = MarketContextBuilder()

    context = builder.build(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        market_structure=make_market_structure(),
        trend=make_trend(),
    )

    assert isinstance(context, MarketContext)
    assert context.instrument.code == "XAUUSD"
    assert context.timeframe == Timeframe.M5
    assert context.market_structure is not None
    assert context.trend is not None


def test_build_market_context_without_optional_values() -> None:

    builder = MarketContextBuilder()

    context = builder.build(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
    )

    assert context.market_structure is None
    assert context.trend is None