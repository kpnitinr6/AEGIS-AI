"""
Tests for the BreakOfStructure domain object.
"""

from dataclasses import FrozenInstanceError
from datetime import datetime, timezone
from decimal import Decimal

import pytest

from backend.domain import (
    ChangeOfCharacter,
    Candle,
    Instrument,
    Price,
    StructurePoint,
    StructureType,
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

def make_price() -> Price:

    return Price(
        instrument=Instrument(
            code="XAUUSD",
            name="Gold Spot",
        ),
        amount=Decimal("3362"),
        time=Time(
            datetime(
                2026,
                7,
                2,
                9,
                5,
                tzinfo=timezone.utc,
            )
        ),
    )


def make_swing() -> Swing:

    return Swing(
        candle=make_candle(),
        type=SwingType.HIGH,
    )


def make_structure_point() -> StructurePoint:

    return StructurePoint(
        structure=StructureType.HIGHER_HIGH,
        swing=make_swing(),
    )



def test_create_valid_change_of_character() -> None:

    choch = ChangeOfCharacter(
        instrument=Instrument(
            code="XAUUSD",
            name="Gold Spot",
        ),
        timeframe=Timeframe.M5,
        broken_structure=make_structure_point(),
        confirming_candle=make_candle(),
        break_price=make_price(),
    )

    assert choch.instrument.code == "XAUUSD"
    assert choch.timeframe == Timeframe.M5
    assert choch.break_price.amount == Decimal("3362")
    assert (
            choch.broken_structure.structure
            == StructureType.HIGHER_HIGH
    )


def test_invalid_instrument() -> None:

    with pytest.raises(TypeError):
        ChangeOfCharacter(
            instrument="XAUUSD",
            timeframe=Timeframe.M5,
            broken_structure=make_structure_point(),
            confirming_candle=make_candle(),
            break_price=make_price(),
        )


def test_invalid_timeframe() -> None:

    with pytest.raises(TypeError):
        ChangeOfCharacter(
            instrument=Instrument(
                code="XAUUSD",
                name="Gold Spot",
            ),
            timeframe="M5",
            broken_structure=make_structure_point(),
            confirming_candle=make_candle(),
            break_price=make_price(),
        )


def test_invalid_structure_point() -> None:

    with pytest.raises(TypeError):
        ChangeOfCharacter(
            instrument=Instrument(
                code="XAUUSD",
                name="Gold Spot",
            ),
            timeframe=Timeframe.M5,
            broken_structure="invalid",
            confirming_candle=make_candle(),
            break_price=make_price(),
        )


def test_invalid_confirming_candle() -> None:

    with pytest.raises(TypeError):
        ChangeOfCharacter(
            instrument=Instrument(
                code="XAUUSD",
                name="Gold Spot",
            ),
            timeframe=Timeframe.M5,
            broken_structure=make_structure_point(),
            confirming_candle="invalid",
            break_price=make_price(),
        )


def test_invalid_break_price() -> None:

    with pytest.raises(TypeError):
        ChangeOfCharacter(
            instrument=Instrument(
                code="XAUUSD",
                name="Gold Spot",
            ),
            timeframe=Timeframe.M5,
            broken_structure=make_structure_point(),
            confirming_candle=make_candle(),
            break_price="3362",
        )


def test_change_of_structure_is_immutable() -> None:

    choch = ChangeOfCharacter(
        instrument=Instrument(
            code="XAUUSD",
            name="Gold Spot",
        ),
        timeframe=Timeframe.M5,
        broken_structure=make_structure_point(),
        confirming_candle=make_candle(),
        break_price=make_price(),
    )

    with pytest.raises(FrozenInstanceError):
        choch.break_price = make_price()