"""
Tests for LiquiditySweepDetector.
"""

from datetime import datetime, timezone
from decimal import Decimal

import pytest

from backend.domain import (
    Candle,
    CandleSeries,
    Instrument,
    LiquiditySweep,
    LiquiditySweepDirection,
    Swing,
    SwingType,
    Time,
    Timeframe,
)
from backend.perception.liquidity_sweep_detector import (
    LiquiditySweepDetector,
)


def make_candle(
    *,
    minute: int,
    high: str,
    low: str,
    close: str,
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
                6,
                9,
                minute,
                tzinfo=timezone.utc,
            )
        ),
        open=Decimal(close),
        high=Decimal(high),
        low=Decimal(low),
        close=Decimal(close),
        tick_volume=100,
    )


def test_invalid_swings_argument() -> None:

    detector = LiquiditySweepDetector()

    with pytest.raises(TypeError):
        detector.detect(
            "invalid",
            CandleSeries(),
        )


def test_invalid_candle_series_argument() -> None:

    detector = LiquiditySweepDetector()

    with pytest.raises(TypeError):
        detector.detect(
            [],
            "invalid",
        )


def test_detects_bullish_liquidity_sweep() -> None:

    swing_candle = make_candle(
        minute=0,
        high="3360",
        low="3340",
        close="3350",
    )

    sweep_candle = make_candle(
        minute=5,
        high="3362",
        low="3338",
        close="3345",
    )

    series = CandleSeries()
    series.add(swing_candle)
    series.add(sweep_candle)

    swing = Swing(
        candle=swing_candle,
        type=SwingType.LOW,
    )

    sweeps = LiquiditySweepDetector().detect(
        [swing],
        series,
    )

    assert len(sweeps) == 1

    sweep = sweeps[0]

    assert isinstance(
        sweep,
        LiquiditySweep,
    )

    assert (
        sweep.direction
        == LiquiditySweepDirection.BULLISH
    )

    assert sweep.swept_swing == swing
    assert sweep.sweep_candle == sweep_candle


def test_detects_bearish_liquidity_sweep() -> None:

    swing_candle = make_candle(
        minute=0,
        high="3360",
        low="3340",
        close="3350",
    )

    sweep_candle = make_candle(
        minute=5,
        high="3365",
        low="3345",
        close="3355",
    )

    series = CandleSeries()
    series.add(swing_candle)
    series.add(sweep_candle)

    swing = Swing(
        candle=swing_candle,
        type=SwingType.HIGH,
    )

    sweeps = LiquiditySweepDetector().detect(
        [swing],
        series,
    )

    assert len(sweeps) == 1

    assert (
        sweeps[0].direction
        == LiquiditySweepDirection.BEARISH
    )


def test_returns_empty_when_no_sweep_exists() -> None:

    swing_candle = make_candle(
        minute=0,
        high="3360",
        low="3340",
        close="3350",
    )

    next_candle = make_candle(
        minute=5,
        high="3358",
        low="3342",
        close="3350",
    )

    series = CandleSeries()
    series.add(swing_candle)
    series.add(next_candle)

    swing = Swing(
        candle=swing_candle,
        type=SwingType.HIGH,
    )

    sweeps = LiquiditySweepDetector().detect(
        [swing],
        series,
    )

    assert sweeps == []