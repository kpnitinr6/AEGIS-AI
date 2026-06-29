"""
Tests for the MarketStructure domain object.
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
)


def make_candle(
    *,
    high: str = "3355.00",
    low: str = "3348.00",
    close: str = "3352.00",
    minute: int = 30,
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
        open=Decimal("3350.00"),
        high=Decimal(high),
        low=Decimal(low),
        close=Decimal(close),
        tick_volume=1000,
    )


def make_structure_point() -> StructurePoint:
    return StructurePoint(
        structure=StructureType.HIGHER_HIGH,
        swing=Swing(
            candle=make_candle(),
            type=SwingType.HIGH,
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


def test_create_empty_market_structure() -> None:
    market = make_market_structure()

    assert len(market) == 0
    assert market.latest() is None
    assert market.previous() is None


def test_append_structure_point() -> None:
    market = make_market_structure()

    point = make_structure_point()

    market.append(point)

    assert len(market) == 1
    assert market.latest() == point
    assert market.previous() is None


def test_previous_returns_second_last_point() -> None:
    market = make_market_structure()

    first = make_structure_point()

    second = StructurePoint(
        structure=StructureType.HIGHER_LOW,
        swing=Swing(
            candle=make_candle(
                high="3345.00",
                low="3340.00",
                close="3342.00",
                minute=45,
            ),
            type=SwingType.LOW,
        ),
    )

    market.append(first)
    market.append(second)

    assert market.latest() == second
    assert market.previous() == first


def test_invalid_append() -> None:
    market = make_market_structure()

    with pytest.raises(TypeError):
        market.append("not a structure point")


def test_invalid_instrument() -> None:
    with pytest.raises(TypeError):
        MarketStructure(
            instrument="XAUUSD",
            timeframe=Timeframe.M5,
        )


def test_invalid_timeframe() -> None:
    with pytest.raises(TypeError):
        MarketStructure(
            instrument=Instrument(
                code="XAUUSD",
                name="Gold Spot",
            ),
            timeframe="M5",
        )


def test_invalid_structure_points_list() -> None:
    with pytest.raises(TypeError):
        MarketStructure(
            instrument=Instrument(
                code="XAUUSD",
                name="Gold Spot",
            ),
            timeframe=Timeframe.M5,
            structure_points=["invalid"],
        )