"""
Tests for the Trend domain object.
"""

from dataclasses import FrozenInstanceError
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
    Trend,
    TrendState,
)


def make_market_structure() -> MarketStructure:
    market = MarketStructure(
        instrument=Instrument(
            code="XAUUSD",
            name="Gold Spot",
        ),
        timeframe=Timeframe.M5,
    )

    point = StructurePoint(
        structure=StructureType.HIGHER_HIGH,
        swing=Swing(
            timeframe=Timeframe.M5,
            type=SwingType.HIGH,
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

    market.append(point)

    return market


def test_create_valid_trend() -> None:
    trend = Trend(
        state=TrendState.BULLISH,
        market_structure=make_market_structure(),
    )

    assert trend.state == TrendState.BULLISH


def test_invalid_state() -> None:
    with pytest.raises(TypeError):
        Trend(
            state="BULLISH",
            market_structure=make_market_structure(),
        )


def test_invalid_market_structure() -> None:
    with pytest.raises(TypeError):
        Trend(
            state=TrendState.BULLISH,
            market_structure="invalid",
        )


def test_trend_is_immutable() -> None:
    trend = Trend(
        state=TrendState.BULLISH,
        market_structure=make_market_structure(),
    )

    with pytest.raises(FrozenInstanceError):
        trend.state = TrendState.BEARISH