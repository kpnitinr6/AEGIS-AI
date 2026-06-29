"""
Tests for the Trend domain object.
"""

from dataclasses import FrozenInstanceError
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
    Trend,
    TrendState,
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
                6,
                29,
                9,
                30,
                tzinfo=timezone.utc,
            )
        ),
        open=Decimal("3350.00"),
        high=Decimal("3355.00"),
        low=Decimal("3348.00"),
        close=Decimal("3352.00"),
        tick_volume=1000,
    )


def make_market_structure() -> MarketStructure:
    market = MarketStructure(
        instrument=Instrument(
            code="XAUUSD",
            name="Gold Spot",
        ),
        timeframe=Timeframe.M5,
    )

    market.append(
        StructurePoint(
            structure=StructureType.HIGHER_HIGH,
            swing=Swing(
                candle=make_candle(),
                type=SwingType.HIGH,
            ),
        )
    )

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