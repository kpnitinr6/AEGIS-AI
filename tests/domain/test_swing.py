"""
Tests for the Swing domain object.
"""

from dataclasses import FrozenInstanceError
from datetime import datetime, timezone
from decimal import Decimal

import pytest

from backend.domain import (
    Candle,
    Instrument,
    Swing,
    SwingType,
    Time,
    Timeframe,
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


def test_create_valid_swing() -> None:
    swing = Swing(
        candle=make_candle(),
        type=SwingType.HIGH,
    )

    assert swing.type == SwingType.HIGH
    assert swing.candle.high == Decimal("3355.00")


def test_invalid_candle() -> None:
    with pytest.raises(TypeError):
        Swing(
            candle="not a candle",
            type=SwingType.HIGH,
        )


def test_invalid_type() -> None:
    with pytest.raises(TypeError):
        Swing(
            candle=make_candle(),
            type="HIGH",
        )


def test_swing_is_immutable() -> None:
    swing = Swing(
        candle=make_candle(),
        type=SwingType.HIGH,
    )

    with pytest.raises(FrozenInstanceError):
        swing.type = SwingType.LOW

def test_swing_references_original_candle() -> None:

    candle = make_candle()

    swing = Swing(

        candle=candle,

        type=SwingType.HIGH,

    )

    assert swing.candle is candle