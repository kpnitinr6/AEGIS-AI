"""
Tests for TrendAnalyzer.
"""

from datetime import datetime, timezone
from decimal import Decimal

import pytest

from backend.domain import (
    Candle,
    Instrument,
    MarketStructure,
    StructurePoint,
    StructureType,
    Swing,
    SwingType,
    Time,
    Timeframe,
    TrendState,
)

from backend.services.trend_analyzer import TrendAnalyzer


def make_candle(
    *,
    high: str,
    low: str,
    close: str,
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
                6,
                29,
                9,
                minute,
                tzinfo=timezone.utc,
            )
        ),
        open=Decimal(close),
        high=Decimal(high),
        low=Decimal(low),
        close=Decimal(close),
        tick_volume=1000,
    )


def make_point(structure: StructureType) -> StructurePoint:

    if structure in (
        StructureType.HIGHER_HIGH,
        StructureType.LOWER_HIGH,
    ):
        swing = Swing(
            candle=make_candle(
                high="3355.00",
                low="3348.00",
                close="3352.00",
                minute=30,
            ),
            type=SwingType.HIGH,
        )
    else:
        swing = Swing(
            candle=make_candle(
                high="3345.00",
                low="3340.00",
                close="3342.00",
                minute=45,
            ),
            type=SwingType.LOW,
        )

    return StructurePoint(
        structure=structure,
        swing=swing,
    )


def make_market_structure() -> MarketStructure:
    return MarketStructure(
        instrument=Instrument(
            code="XAUUSD",
            name="Gold Spot",
        ),
        timeframe=Timeframe.M5,
    )


def test_empty_market_returns_unknown() -> None:
    analyzer = TrendAnalyzer()

    trend = analyzer.analyze(
        make_market_structure()
    )

    assert trend.state == TrendState.UNKNOWN


def test_bullish_market() -> None:
    market = make_market_structure()

    market.append(make_point(StructureType.HIGHER_HIGH))
    market.append(make_point(StructureType.HIGHER_LOW))

    analyzer = TrendAnalyzer()

    trend = analyzer.analyze(market)

    assert trend.state == TrendState.BULLISH


def test_bearish_market() -> None:
    market = make_market_structure()

    market.append(make_point(StructureType.LOWER_HIGH))
    market.append(make_point(StructureType.LOWER_LOW))

    analyzer = TrendAnalyzer()

    trend = analyzer.analyze(market)

    assert trend.state == TrendState.BEARISH


def test_sideways_market() -> None:
    market = make_market_structure()

    market.append(make_point(StructureType.HIGHER_HIGH))
    market.append(make_point(StructureType.LOWER_LOW))

    analyzer = TrendAnalyzer()

    trend = analyzer.analyze(market)

    assert trend.state == TrendState.SIDEWAYS


def test_invalid_subject() -> None:
    analyzer = TrendAnalyzer()

    with pytest.raises(TypeError):
        analyzer.analyze("invalid")