"""
Tests for the BOSReasoner.
"""

from datetime import datetime, timezone
from decimal import Decimal

from backend.domain import (
    BreakOfStructure,
    Candle,
    EvidenceDirection,
    EvidenceSource,
    Instrument,
    MarketContext,
    MarketStructure,
    Price,
    StructurePoint,
    StructureType,
    Swing,
    SwingType,
    Time,
    Timeframe,
)
from backend.reasoning import BOSReasoner


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
                3,
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


def make_bos(
    structure: StructureType,
) -> BreakOfStructure:

    candle = make_candle()

    point = StructurePoint(
        structure=structure,
        swing=Swing(
            candle=candle,
            type=SwingType.HIGH,
        ),
    )

    return BreakOfStructure(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        broken_structure=point,
        confirming_candle=candle,
        break_price=Price(
            instrument=make_instrument(),
            amount=candle.close,
            time=candle.open_time,
        ),
    )


def test_bullish_bos_produces_bullish_evidence() -> None:

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        break_of_structures=[
            make_bos(
                StructureType.HIGHER_HIGH,
            )
        ],
    )

    evidence = BOSReasoner().evaluate(context)

    assert len(evidence) == 1
    assert evidence[0].source == EvidenceSource.BREAK_OF_STRUCTURE
    assert evidence[0].direction == EvidenceDirection.BULLISH


def test_bearish_bos_produces_bearish_evidence() -> None:

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        break_of_structures=[
            make_bos(
                StructureType.LOWER_HIGH,
            )
        ],
    )

    evidence = BOSReasoner().evaluate(context)

    assert len(evidence) == 1
    assert evidence[0].source == EvidenceSource.BREAK_OF_STRUCTURE
    assert evidence[0].direction == EvidenceDirection.BEARISH


def test_no_bos_produces_no_evidence() -> None:

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
    )

    assert BOSReasoner().evaluate(context) == []