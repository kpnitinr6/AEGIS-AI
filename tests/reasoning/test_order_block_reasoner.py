"""
Tests for OrderBlockReasoner.
"""

from datetime import datetime, timezone
from decimal import Decimal

from backend.domain import (
    Candle,
    Instrument,
    MarketContext,
    OrderBlock,
    OrderBlockDirection,
    Time,
    Timeframe,
    EvidenceDirection,
    EvidenceSource,
)
from backend.reasoning import (
    OrderBlockReasoner,
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
                8,
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


def make_order_block(
    direction: OrderBlockDirection,
) -> OrderBlock:

    return OrderBlock(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        direction=direction,
        origin_candle=make_candle(),
    )


def test_bullish_order_block_produces_bullish_evidence() -> None:

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        order_blocks=[
            make_order_block(
                OrderBlockDirection.BULLISH,
            )
        ],
    )

    evidence = OrderBlockReasoner().evaluate(
        context,
    )

    assert len(evidence) == 1
    assert (
        evidence[0].source
        == EvidenceSource.ORDER_BLOCK
    )
    assert (
        evidence[0].direction
        == EvidenceDirection.BULLISH
    )


def test_bearish_order_block_produces_bearish_evidence() -> None:

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        order_blocks=[
            make_order_block(
                OrderBlockDirection.BEARISH,
            )
        ],
    )

    evidence = OrderBlockReasoner().evaluate(
        context,
    )

    assert len(evidence) == 1
    assert (
        evidence[0].direction
        == EvidenceDirection.BEARISH
    )


def test_no_order_blocks_returns_no_evidence() -> None:

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
    )

    assert (
        OrderBlockReasoner().evaluate(
            context,
        )
        == []
    )