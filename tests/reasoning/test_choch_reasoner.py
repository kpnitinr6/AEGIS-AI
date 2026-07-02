"""
Tests for CHOCHReasoner.
"""

from datetime import datetime, timezone
from decimal import Decimal

from backend.domain import (
    Candle,
    ChangeOfCharacter,
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
from backend.reasoning import CHOCHReasoner


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
                4,
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


def make_choch(
    structure: StructureType,
) -> ChangeOfCharacter:

    candle = make_candle()

    point = StructurePoint(
        structure=structure,
        swing=Swing(
            candle=candle,
            type=SwingType.HIGH,
        ),
    )

    return ChangeOfCharacter(
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


def test_bullish_choch_produces_bullish_evidence() -> None:

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        change_of_characters=[
            make_choch(
                StructureType.LOWER_LOW,
            )
        ],
    )

    evidence = CHOCHReasoner().evaluate(context)

    assert len(evidence) == 1
    assert (
        evidence[0].source
        == EvidenceSource.CHANGE_OF_CHARACTER
    )
    assert (
        evidence[0].direction
        == EvidenceDirection.BULLISH
    )


def test_bearish_choch_produces_bearish_evidence() -> None:

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        change_of_characters=[
            make_choch(
                StructureType.HIGHER_HIGH,
            )
        ],
    )

    evidence = CHOCHReasoner().evaluate(context)

    assert len(evidence) == 1
    assert (
        evidence[0].source
        == EvidenceSource.CHANGE_OF_CHARACTER
    )
    assert (
        evidence[0].direction
        == EvidenceDirection.BEARISH
    )


def test_no_choch_produces_no_evidence() -> None:

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
    )

    assert CHOCHReasoner().evaluate(context) == []