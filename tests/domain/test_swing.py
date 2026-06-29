"""
Tests for the Swing domain object.
"""
from datetime import datetime, timezone
from dataclasses import FrozenInstanceError
from decimal import Decimal


import pytest

from backend.domain import (
    Instrument,
    Price,
    Swing,
    SwingType,
    Time,
    Timeframe,
)


def make_price() -> Price:
    """Create a valid Price object for testing."""
    return Price(
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
    )


def test_create_valid_swing() -> None:
    """A valid Swing should be created successfully."""

    swing = Swing(
        timeframe=Timeframe.M5,
        type=SwingType.HIGH,
        price=make_price(),
    )

    assert swing.timeframe == Timeframe.M5
    assert swing.type == SwingType.HIGH
    assert swing.price.amount == Decimal("3350.50")


def test_invalid_timeframe() -> None:
    """Swing should reject an invalid timeframe."""

    with pytest.raises(TypeError):
        Swing(
            timeframe="M5",
            type=SwingType.HIGH,
            price=make_price(),
        )


def test_invalid_swing_type() -> None:
    """Swing should reject an invalid swing type."""

    with pytest.raises(TypeError):
        Swing(
            timeframe=Timeframe.M5,
            type="HIGH",
            price=make_price(),
        )


def test_invalid_price() -> None:
    """Swing should reject an invalid Price."""

    with pytest.raises(TypeError):
        Swing(
            timeframe=Timeframe.M5,
            type=SwingType.HIGH,
            price="3350.50",
        )


def test_swing_is_immutable() -> None:
    """Swing must be immutable."""

    swing = Swing(
        timeframe=Timeframe.M5,
        type=SwingType.HIGH,
        price=make_price(),
    )

    with pytest.raises(FrozenInstanceError):
        swing.type = SwingType.LOW