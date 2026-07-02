"""
Tests for OrderBlockDetector.
"""

from datetime import datetime, timezone
from decimal import Decimal

import pytest

from backend.domain import (
    BreakOfStructure,
    Candle,
    CandleSeries,
    Instrument,
    OrderBlock,
    OrderBlockDirection,
    Price,
    StructurePoint,
    StructureType,
    Swing,
    SwingType,
    Time,
    Timeframe,
)
from backend.perception.order_block_detector import (
    OrderBlockDetector,
)


def make_instrument() -> Instrument:
    return Instrument(
        code="XAUUSD",
        name="Gold Spot",
    )


def make_candle(
    *,
    minute: int,
    bullish: bool,
) -> Candle:

    if bullish:
        open_price = Decimal("3350")
        close_price = Decimal("3360")
    else:
        open_price = Decimal("3360")
        close_price = Decimal("3350")

    return Candle(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        open_time=Time(
            datetime(
                2026,
                7,
                8,
                9,
                minute,
                tzinfo=timezone.utc,
            )
        ),
        open=open_price,
        high=Decimal("3365"),
        low=Decimal("3345"),
        close=close_price,
        tick_volume=100,
    )


def make_bos(
    confirming_candle: Candle,
) -> BreakOfStructure:

    swing = Swing(
        candle=confirming_candle,
        type=SwingType.HIGH,
    )

    point = StructurePoint(
        structure=StructureType.HIGHER_HIGH,
        swing=swing,
    )

    return BreakOfStructure(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        broken_structure=point,
        confirming_candle=confirming_candle,
        break_price=Price(
            instrument=make_instrument(),
            amount=confirming_candle.close,
            time=confirming_candle.open_time,
        ),
    )


def test_invalid_candle_series() -> None:

    with pytest.raises(TypeError):
        OrderBlockDetector().detect(
            "invalid",
            make_bos(
                make_candle(
                    minute=5,
                    bullish=True,
                )
            ),
        )


def test_invalid_break_of_structure() -> None:

    with pytest.raises(TypeError):
        OrderBlockDetector().detect(
            CandleSeries(),
            "invalid",
        )


def test_detect_bullish_order_block() -> None:

    series = CandleSeries()

    bearish = make_candle(
        minute=0,
        bullish=False,
    )

    bullish_bos = make_candle(
        minute=5,
        bullish=True,
    )

    series.add(bearish)
    series.add(bullish_bos)

    order_block = OrderBlockDetector().detect(
        series,
        make_bos(
            bullish_bos,
        ),
    )

    assert isinstance(
        order_block,
        OrderBlock,
    )

    assert (
        order_block.direction
        == OrderBlockDirection.BULLISH
    )

    assert (
        order_block.origin_candle
        == bearish
    )


def test_returns_none_when_previous_candle_not_bearish() -> None:

    series = CandleSeries()

    bullish1 = make_candle(
        minute=0,
        bullish=True,
    )

    bullish2 = make_candle(
        minute=5,
        bullish=True,
    )

    series.add(bullish1)
    series.add(bullish2)

    assert (
        OrderBlockDetector().detect(
            series,
            make_bos(
                bullish2,
            ),
        )
        is None
    )


def test_returns_none_when_confirmation_is_first_candle() -> None:

    series = CandleSeries()

    bullish = make_candle(
        minute=0,
        bullish=True,
    )

    series.add(
        bullish,
    )

    assert (
        OrderBlockDetector().detect(
            series,
            make_bos(
                bullish,
            ),
        )
        is None
    )