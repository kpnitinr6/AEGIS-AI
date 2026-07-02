"""
Tests for OrderBlock.
"""

from datetime import datetime, timezone
from decimal import Decimal

import pytest

from backend.domain import (
    Candle,
    Instrument,
    OrderBlock,
    OrderBlockDirection,
    Time,
    Timeframe,
)


def make_instrument() -> Instrument:
    return Instrument(
        code="XAUUSD",
        name="Gold Spot",
    )


def make_candle() -> Candle:
    return Candle(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        open_time=Time(
            datetime(
                2026,
                7,
                7,
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


def test_create_order_block() -> None:

    order_block = OrderBlock(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        direction=OrderBlockDirection.BULLISH,
        origin_candle=make_candle(),
    )

    assert (
        order_block.instrument.code
        == "XAUUSD"
    )

    assert (
        order_block.direction
        == OrderBlockDirection.BULLISH
    )


def test_invalid_direction() -> None:

    with pytest.raises(TypeError):

        OrderBlock(
            instrument=make_instrument(),
            timeframe=Timeframe.M5,
            direction="BULLISH",
            origin_candle=make_candle(),
        )


def test_invalid_origin_candle() -> None:

    with pytest.raises(TypeError):

        OrderBlock(
            instrument=make_instrument(),
            timeframe=Timeframe.M5,
            direction=OrderBlockDirection.BULLISH,
            origin_candle="invalid",
        )