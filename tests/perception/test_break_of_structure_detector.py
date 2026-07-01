"""
Tests for BreakOfStructureDetector.
"""

from datetime import datetime, timezone
from decimal import Decimal

import pytest

from backend.domain import (
    BreakOfStructure,
    Candle,
    Instrument,
    MarketStructure,
    Price,
    StructurePoint,
    StructureType,
    Swing,
    SwingType,
    Time,
    Timeframe,
)
from backend.perception.break_of_structure_detector import (
    BreakOfStructureDetector,
)


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
                3,
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
        candle = make_candle(
            high="3360",
            low="3340",
            minute=0,
        )
        swing_type = SwingType.HIGH

    else:
        candle = make_candle(
            high="3355",
            low="3335",
            minute=5,
        )
        swing_type = SwingType.LOW

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

    detector = BreakOfStructureDetector()

    with pytest.raises(TypeError):
        detector.detect("invalid")


def test_empty_market_returns_none() -> None:

    detector = BreakOfStructureDetector()

    market = make_market()

    assert detector.detect(market) is None


def test_bullish_break_of_structure() -> None:

    detector = BreakOfStructureDetector()

    market = make_market(
        StructureType.HIGHER_HIGH,
        StructureType.HIGHER_LOW,
    )

    event = detector.detect(market)

    assert isinstance(
        event,
        BreakOfStructure,
    )

    assert (
        event.instrument.code
        == "XAUUSD"
    )

    assert (
        event.timeframe
        == Timeframe.M5
    )

    assert (
        event.broken_structure
        == market.previous()
    )

    assert isinstance(
        event.break_price,
        Price,
    )


def test_bearish_break_of_structure() -> None:

    detector = BreakOfStructureDetector()

    market = make_market(
        StructureType.LOWER_HIGH,
        StructureType.LOWER_LOW,
    )

    event = detector.detect(market)

    assert isinstance(
        event,
        BreakOfStructure,
    )

    assert (
        event.broken_structure
        == market.previous()
    )


def test_no_break_of_structure() -> None:

    detector = BreakOfStructureDetector()

    market = make_market(
        StructureType.HIGHER_HIGH,
        StructureType.LOWER_LOW,
    )

    assert detector.detect(market) is None