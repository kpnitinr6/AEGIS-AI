"""
Tests for the LiquiditySweep domain object.
"""

from dataclasses import FrozenInstanceError
from datetime import datetime, timezone
from decimal import Decimal

import pytest

from backend.domain import (
    Candle,
    Instrument,
    LiquiditySweep,
    LiquiditySweepDirection,
    Price,
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


def make_swing() -> Swing:

    return Swing(
        candle=make_candle(),
        type=SwingType.LOW,
    )


def test_create_valid_liquidity_sweep() -> None:

    sweep = LiquiditySweep(
        direction=LiquiditySweepDirection.BULLISH,
        swept_swing=make_swing(),
        sweep_candle=make_candle(),
    )

    assert (
        sweep.direction
        == LiquiditySweepDirection.BULLISH
    )


def test_invalid_direction() -> None:

    with pytest.raises(TypeError):
        LiquiditySweep(
            direction="BULLISH",
            swept_swing=make_swing(),
            sweep_candle=make_candle(),
        )


def test_invalid_swing() -> None:

    with pytest.raises(TypeError):
        LiquiditySweep(
            direction=LiquiditySweepDirection.BULLISH,
            swept_swing="invalid",
            sweep_candle=make_candle(),
        )


def test_invalid_candle() -> None:

    with pytest.raises(TypeError):
        LiquiditySweep(
            direction=LiquiditySweepDirection.BULLISH,
            swept_swing=make_swing(),
            sweep_candle="invalid",
        )


def test_liquidity_sweep_is_immutable() -> None:

    sweep = LiquiditySweep(
        direction=LiquiditySweepDirection.BULLISH,
        swept_swing=make_swing(),
        sweep_candle=make_candle(),
    )

    with pytest.raises(FrozenInstanceError):
        sweep.direction = (
            LiquiditySweepDirection.BEARISH
        )