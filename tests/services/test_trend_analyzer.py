"""
Tests for TrendAnalyzer.
"""

from datetime import datetime, timezone
from decimal import Decimal

import pytest

from backend.domain import (
    Instrument,
    MarketStructure,
    Price,
    StructurePoint,
    StructureType,
    Swing,
    SwingType,
    Time,
    Timeframe,
    TrendState,
)

from backend.services.trend_analyzer import TrendAnalyzer


def make_point(structure: StructureType) -> StructurePoint:

    swing_type = (
        SwingType.HIGH
        if structure in (
            StructureType.HIGHER_HIGH,
            StructureType.LOWER_HIGH,
        )
        else SwingType.LOW
    )

    return StructurePoint(
        structure=structure,
        swing=Swing(
            timeframe=Timeframe.M5,
            type=swing_type,
            price=Price(
                instrument=Instrument(
                    code="XAUUSD",
                    name="Gold Spot",
                ),
                amount=Decimal("3350.50"),
                time=Time(
                    datetime(
                        2026,
                        6,
                        29,
                        9,
                        30,
                        tzinfo=timezone.utc,
                    )
                ),
            ),
        ),
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

    market.append(
        make_point(
            StructureType.HIGHER_HIGH
        )
    )

    market.append(
        make_point(
            StructureType.HIGHER_LOW
        )
    )

    analyzer = TrendAnalyzer()

    trend = analyzer.analyze(market)

    assert trend.state == TrendState.BULLISH


def test_bearish_market() -> None:

    market = make_market_structure()

    market.append(
        make_point(
            StructureType.LOWER_HIGH
        )
    )

    market.append(
        make_point(
            StructureType.LOWER_LOW
        )
    )

    analyzer = TrendAnalyzer()

    trend = analyzer.analyze(market)

    assert trend.state == TrendState.BEARISH


def test_sideways_market() -> None:

    market = make_market_structure()

    market.append(
        make_point(
            StructureType.HIGHER_HIGH
        )
    )

    market.append(
        make_point(
            StructureType.LOWER_LOW
        )
    )

    analyzer = TrendAnalyzer()

    trend = analyzer.analyze(market)

    assert trend.state == TrendState.SIDEWAYS


def test_invalid_subject() -> None:

    analyzer = TrendAnalyzer()

    with pytest.raises(TypeError):
        analyzer.analyze("invalid")