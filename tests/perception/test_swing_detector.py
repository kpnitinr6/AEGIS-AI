"""
Tests for the SwingDetector.
"""

from datetime import datetime, timedelta, timezone
from decimal import Decimal

import pytest

from backend.domain import (
    Candle,
    CandleSeries,
    Instrument,
    SwingType,
    Time,
    Timeframe,
)
from backend.perception import SwingDetector


def make_candle(
    *,
    high: str,
    low: str,
    close: str,
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
                6,
                30,
                9,
                minute,
                tzinfo=timezone.utc,
            )
        ),
        open=Decimal(close),
        high=Decimal(high),
        low=Decimal(low),
        close=Decimal(close),
        tick_volume=1000,
    )


def make_series(candles: list[Candle]) -> CandleSeries:
    series = CandleSeries()

    for candle in candles:
        series.add(candle)

    return series


def test_invalid_subject() -> None:
    detector = SwingDetector()

    with pytest.raises(TypeError):
        detector.detect("invalid")


def test_empty_series_returns_no_swings() -> None:
    detector = SwingDetector()

    swings = detector.detect(CandleSeries())

    assert swings == []


def test_two_candles_return_no_swings() -> None:
    detector = SwingDetector()

    series = make_series(
        [
            make_candle(
                high="3350",
                low="3345",
                close="3348",
                minute=0,
            ),
            make_candle(
                high="3352",
                low="3347",
                close="3350",
                minute=5,
            ),
        ]
    )

    swings = detector.detect(series)

    assert swings == []


def test_detect_single_swing_high() -> None:
    detector = SwingDetector()

    series = make_series(
        [
            make_candle(
                high="3350",
                low="3345",
                close="3348",
                minute=0,
            ),
            make_candle(
                high="3360",
                low="3348",
                close="3355",
                minute=5,
            ),
            make_candle(
                high="3352",
                low="3347",
                close="3350",
                minute=10,
            ),
        ]
    )

    swings = detector.detect(series)

    assert len(swings) == 1
    assert swings[0].type == SwingType.HIGH
    assert swings[0].candle.high == Decimal("3360")


def test_detect_single_swing_low() -> None:
    detector = SwingDetector()

    series = make_series(
        [
            make_candle(
                high="3355",
                low="3348",
                close="3352",
                minute=0,
            ),
            make_candle(
                high="3350",
                low="3340",
                close="3342",
                minute=5,
            ),
            make_candle(
                high="3354",
                low="3346",
                close="3351",
                minute=10,
            ),
        ]
    )

    swings = detector.detect(series)

    assert len(swings) == 1
    assert swings[0].type == SwingType.LOW
    assert swings[0].candle.low == Decimal("3340")


def test_detect_multiple_swings() -> None:
    detector = SwingDetector()

    series = make_series(
        [
            make_candle(high="3350", low="3345", close="3348", minute=0),
            make_candle(high="3360", low="3348", close="3358", minute=5),   # HIGH
            make_candle(high="3350", low="3340", close="3342", minute=10),  # LOW
            make_candle(high="3362", low="3347", close="3359", minute=15),  # HIGH
            make_candle(high="3355", low="3348", close="3350", minute=20),
        ]
    )

    swings = detector.detect(series)

    assert len(swings) == 3

    assert swings[0].type == SwingType.HIGH
    assert swings[1].type == SwingType.LOW
    assert swings[2].type == SwingType.HIGH