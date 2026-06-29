"""
Tests for the StructurePoint domain object.
"""

from dataclasses import FrozenInstanceError
from datetime import datetime, timezone
from decimal import Decimal

import pytest

from backend.domain import (
    Instrument,
    Price,
    StructurePoint,
    StructureType,
    Swing,
    SwingType,
    Time,
    Timeframe,
)


def make_swing() -> Swing:
    return Swing(
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
    )


def test_create_valid_structure_point() -> None:
    point = StructurePoint(
        structure=StructureType.HIGHER_HIGH,
        swing=make_swing(),
    )

    assert point.structure == StructureType.HIGHER_HIGH
    assert point.swing.type == SwingType.HIGH


def test_invalid_structure_type() -> None:
    with pytest.raises(TypeError):
        StructurePoint(
            structure="HH",
            swing=make_swing(),
        )


def test_invalid_swing() -> None:
    with pytest.raises(TypeError):
        StructurePoint(
            structure=StructureType.HIGHER_HIGH,
            swing="not a swing",
        )


def test_structure_point_is_immutable() -> None:
    point = StructurePoint(
        structure=StructureType.HIGHER_HIGH,
        swing=make_swing(),
    )

    with pytest.raises(FrozenInstanceError):
        point.structure = StructureType.LOWER_HIGH