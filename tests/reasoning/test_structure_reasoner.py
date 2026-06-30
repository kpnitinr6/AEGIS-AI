"""
Tests for the StructureReasoner.
"""

from datetime import datetime, timezone
from decimal import Decimal

from backend.domain import (
    Candle,
    EvidenceDirection,
    EvidenceSource,
    Instrument,
    MarketContext,
    MarketStructure,
    StructurePoint,
    StructureType,
    Swing,
    SwingType,
    Time,
    Timeframe,
)
from backend.reasoning import StructureReasoner


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


def make_market_structure(
    structure_type: StructureType,
) -> MarketStructure:

    structure = MarketStructure(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
    )

    structure.append(
        StructurePoint(
            structure=structure_type,
            swing=Swing(
                candle=make_candle(),
                type=SwingType.HIGH,
            ),
        )
    )

    return structure


def test_higher_high_produces_bullish_evidence() -> None:

    reasoner = StructureReasoner()

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        market_structure=make_market_structure(
            StructureType.HIGHER_HIGH
        ),
    )

    evidence = reasoner.evaluate(context)

    assert len(evidence) == 1
    assert evidence[0].source == EvidenceSource.STRUCTURE
    assert evidence[0].direction == EvidenceDirection.BULLISH
    assert (
        evidence[0].reason
        == "Latest confirmed structure is a Higher High."
    )


def test_higher_low_produces_bullish_evidence() -> None:

    reasoner = StructureReasoner()

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        market_structure=make_market_structure(
            StructureType.HIGHER_LOW
        ),
    )

    evidence = reasoner.evaluate(context)

    assert len(evidence) == 1
    assert evidence[0].source == EvidenceSource.STRUCTURE
    assert evidence[0].direction == EvidenceDirection.BULLISH
    assert (
        evidence[0].reason
        == "Latest confirmed structure is a Higher Low."
    )


def test_lower_high_produces_bearish_evidence() -> None:

    reasoner = StructureReasoner()

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        market_structure=make_market_structure(
            StructureType.LOWER_HIGH
        ),
    )

    evidence = reasoner.evaluate(context)

    assert len(evidence) == 1
    assert evidence[0].source == EvidenceSource.STRUCTURE
    assert evidence[0].direction == EvidenceDirection.BEARISH
    assert (
        evidence[0].reason
        == "Latest confirmed structure is a Lower High."
    )


def test_lower_low_produces_bearish_evidence() -> None:

    reasoner = StructureReasoner()

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        market_structure=make_market_structure(
            StructureType.LOWER_LOW
        ),
    )

    evidence = reasoner.evaluate(context)

    assert len(evidence) == 1
    assert evidence[0].source == EvidenceSource.STRUCTURE
    assert evidence[0].direction == EvidenceDirection.BEARISH
    assert (
        evidence[0].reason
        == "Latest confirmed structure is a Lower Low."
    )


def test_no_market_structure_produces_no_evidence() -> None:

    reasoner = StructureReasoner()

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
    )

    evidence = reasoner.evaluate(context)

    assert evidence == []


def test_empty_market_structure_produces_no_evidence() -> None:

    reasoner = StructureReasoner()

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        market_structure=MarketStructure(
            instrument=make_instrument(),
            timeframe=Timeframe.M5,
        ),
    )

    evidence = reasoner.evaluate(context)

    assert evidence == []