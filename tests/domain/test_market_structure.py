"""
Tests for the MarketStructure domain object.
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
)


def make_structure_point() -> StructurePoint:
    return StructurePoint(
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
            timeframe=Timeframe.M5,
            type=SwingType.LOW,
            price=Price(
                instrument=Instrument(
                    code="XAUUSD",
                    name="Gold Spot",
                ),
                amount=Decimal("3340.00"),
                time=Time(
                    datetime(
                        2026,
                        6,
                        29,
                        9,
                        45,
                        tzinfo=timezone.utc,
                    )
                ),
            ),
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