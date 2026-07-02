"""
Tests for LiquiditySweepReasoner.
"""

from datetime import datetime, timezone
from decimal import Decimal

from backend.domain import (
    Candle,
    EvidenceDirection,
    EvidenceSource,
    Instrument,
    LiquiditySweep,
    LiquiditySweepDirection,
    MarketContext,
    Swing,
    SwingType,
    Time,
    Timeframe,
)
from backend.reasoning import LiquiditySweepReasoner


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
                6,
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


def make_sweep(
    direction: LiquiditySweepDirection,
) -> LiquiditySweep:

    candle = make_candle()

    return LiquiditySweep(
        direction=direction,
        swept_swing=Swing(
            candle=candle,
            type=(
                SwingType.LOW
                if direction == LiquiditySweepDirection.BULLISH
                else SwingType.HIGH
            ),
        ),
        sweep_candle=candle,
    )


def test_bullish_liquidity_sweep_produces_bullish_evidence() -> None:

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        liquidity_sweeps=[
            make_sweep(
                LiquiditySweepDirection.BULLISH,
            )
        ],
    )

    evidence = LiquiditySweepReasoner().evaluate(
        context,
    )

    assert len(evidence) == 1

    assert (
        evidence[0].source
        == EvidenceSource.LIQUIDITY_SWEEP
    )

    assert (
        evidence[0].direction
        == EvidenceDirection.BULLISH
    )

    assert (
        evidence[0].reason
        == "Confirmed bullish liquidity sweep."
    )


def test_bearish_liquidity_sweep_produces_bearish_evidence() -> None:

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        liquidity_sweeps=[
            make_sweep(
                LiquiditySweepDirection.BEARISH,
            )
        ],
    )

    evidence = LiquiditySweepReasoner().evaluate(
        context,
    )

    assert len(evidence) == 1

    assert (
        evidence[0].source
        == EvidenceSource.LIQUIDITY_SWEEP
    )

    assert (
        evidence[0].direction
        == EvidenceDirection.BEARISH
    )

    assert (
        evidence[0].reason
        == "Confirmed bearish liquidity sweep."
    )


def test_no_liquidity_sweeps_produce_no_evidence() -> None:

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
    )

    evidence = LiquiditySweepReasoner().evaluate(
        context,
    )

    assert evidence == []