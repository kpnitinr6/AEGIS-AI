"""
Tests for CHOCHDetector.
"""

from datetime import datetime, timezone
from decimal import Decimal

import pytest

from backend.domain import (
    Candle,
    EvidenceDirection,
    EvidenceSource,
    Instrument,
    MarketStructure,
    StructurePoint,
    StructureType,
    Swing,
    SwingType,
    Time,
    Timeframe,
)

from backend.reasoning import CHOCHDetector


def make_candle(
    *,
    high: str,
    low: str,
    minute: int,
) -> Candle:

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
                1,
                9,
                minute,
                tzinfo=timezone.utc,
            )
        ),
        open=Decimal(low),
        high=Decimal(high),
        low=Decimal(low),
        close=Decimal(high),
        tick_volume=100,
    )


def make_swing(
    structure: StructureType,
) -> Swing:

    if structure in (
        StructureType.HIGHER_HIGH,
        StructureType.LOWER_HIGH,
    ):
        swing_type = SwingType.HIGH
        candle = make_candle(
            high="3360",
            low="3340",
            minute=0,
        )
    else:
        swing_type = SwingType.LOW
        candle = make_candle(
            high="3360",
            low="3340",
            minute=5,
        )

    return Swing(
        candle=candle,
        type=swing_type,
    )


def make_market(
    *structures: StructureType,
) -> MarketStructure:

    market = MarketStructure(
        instrument=Instrument(
            code="XAUUSD",
            name="Gold Spot",
        ),
        timeframe=Timeframe.M5,
    )

    for structure in structures:
        market.append(
            StructurePoint(
                structure=structure,
                swing=make_swing(structure),
            )
        )

    return market


def test_invalid_subject() -> None:

    detector = CHOCHDetector()

    with pytest.raises(TypeError):
        detector.detect("invalid")


def test_empty_market_returns_none() -> None:

    detector = CHOCHDetector()

    market = make_market()

    assert detector.detect(market) is None


def test_bullish_choch() -> None:

    detector = CHOCHDetector()

    market = make_market(
        StructureType.LOWER_LOW,
        StructureType.HIGHER_HIGH,
    )

    evidence = detector.detect(market)

    assert evidence is not None
    assert (
        evidence.source
        == EvidenceSource.CHANGE_OF_CHARACTER
    )
    assert (
        evidence.direction
        == EvidenceDirection.BULLISH
    )


def test_bearish_choch() -> None:

    detector = CHOCHDetector()

    market = make_market(
        StructureType.HIGHER_HIGH,
        StructureType.LOWER_LOW,
    )

    evidence = detector.detect(market)

    assert evidence is not None
    assert (
        evidence.source
        == EvidenceSource.CHANGE_OF_CHARACTER
    )
    assert (
        evidence.direction
        == EvidenceDirection.BEARISH
    )


def test_no_choch() -> None:

    detector = CHOCHDetector()

    market = make_market(
        StructureType.HIGHER_HIGH,
        StructureType.HIGHER_LOW,
    )

    assert detector.detect(market) is None