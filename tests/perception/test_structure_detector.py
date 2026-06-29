"""
Tests for StructureDetector.
"""

from datetime import datetime, timezone
from decimal import Decimal

import pytest

from backend.domain import (
    Candle,
    Instrument,
    MarketStructure,
    StructureType,
    Swing,
    SwingType,
    Time,
    Timeframe,
)
from backend.perception import StructureDetector


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


def make_high(
    high: str,
    minute: int,
) -> Swing:
    return Swing(
        candle=make_candle(
            high=high,
            low="3340",
            minute=minute,
        ),
        type=SwingType.HIGH,
    )


def make_low(
    low: str,
    minute: int,
) -> Swing:
    return Swing(
        candle=make_candle(
            high="3360",
            low=low,
            minute=minute,
        ),
        type=SwingType.LOW,
    )


def test_invalid_subject() -> None:

    detector = StructureDetector()

    with pytest.raises(TypeError):
        detector.detect("invalid")


def test_empty_list() -> None:

    detector = StructureDetector()

    with pytest.raises(ValueError):
        detector.detect([])


def test_returns_market_structure() -> None:

    detector = StructureDetector()

    result = detector.detect(
        [
            make_high("3350", 0),
            make_high("3360", 5),
        ]
    )

    assert isinstance(result, MarketStructure)


def test_detect_higher_high() -> None:

    detector = StructureDetector()

    result = detector.detect(
        [
            make_high("3350", 0),
            make_high("3360", 5),
        ]
    )

    assert len(result) == 2

    assert (
        result.latest().structure
        == StructureType.HIGHER_HIGH
    )


def test_detect_lower_high() -> None:

    detector = StructureDetector()

    result = detector.detect(
        [
            make_high("3360", 0),
            make_high("3350", 5),
        ]
    )

    assert (
        result.latest().structure
        == StructureType.LOWER_HIGH
    )


def test_detect_higher_low() -> None:

    detector = StructureDetector()

    result = detector.detect(
        [
            make_low("3340", 0),
            make_low("3345", 5),
        ]
    )

    assert (
        result.latest().structure
        == StructureType.HIGHER_LOW
    )


def test_detect_lower_low() -> None:

    detector = StructureDetector()

    result = detector.detect(
        [
            make_low("3345", 0),
            make_low("3340", 5),
        ]
    )

    assert (
        result.latest().structure
        == StructureType.LOWER_LOW
    )