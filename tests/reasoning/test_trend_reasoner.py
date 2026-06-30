"""
Tests for the TrendReasoner.
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
    Trend,
    TrendState,
)
from backend.reasoning import TrendReasoner


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


def make_market_structure() -> MarketStructure:
    structure = MarketStructure(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
    )

    structure.append(
        StructurePoint(
            structure=StructureType.HIGHER_HIGH,
            swing=Swing(
                candle=make_candle(),
                type=SwingType.HIGH,
            ),
        )
    )

    return structure


def make_trend(state: TrendState) -> Trend:
    return Trend(
        state=state,
        market_structure=make_market_structure(),
    )


def test_bullish_trend_produces_bullish_evidence() -> None:

    reasoner = TrendReasoner()

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        trend=make_trend(TrendState.BULLISH),
    )

    evidence = reasoner.evaluate(context)

    assert len(evidence) == 1
    assert evidence[0].source == EvidenceSource.TREND
    assert evidence[0].direction == EvidenceDirection.BULLISH
    assert evidence[0].reason == "Confirmed bullish trend."


def test_bearish_trend_produces_bearish_evidence() -> None:

    reasoner = TrendReasoner()

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        trend=make_trend(TrendState.BEARISH),
    )

    evidence = reasoner.evaluate(context)

    assert len(evidence) == 1
    assert evidence[0].source == EvidenceSource.TREND
    assert evidence[0].direction == EvidenceDirection.BEARISH
    assert evidence[0].reason == "Confirmed bearish trend."


def test_sideways_trend_produces_neutral_evidence() -> None:

    reasoner = TrendReasoner()

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        trend=make_trend(TrendState.SIDEWAYS),
    )

    evidence = reasoner.evaluate(context)

    assert len(evidence) == 1
    assert evidence[0].source == EvidenceSource.TREND
    assert evidence[0].direction == EvidenceDirection.NEUTRAL
    assert evidence[0].reason == "Market is moving sideways."


def test_unknown_trend_produces_neutral_evidence() -> None:

    reasoner = TrendReasoner()

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        trend=make_trend(TrendState.UNKNOWN),
    )

    evidence = reasoner.evaluate(context)

    assert len(evidence) == 1
    assert evidence[0].source == EvidenceSource.TREND
    assert evidence[0].direction == EvidenceDirection.NEUTRAL
    assert evidence[0].reason == "Market trend is unknown."


def test_no_trend_produces_no_evidence() -> None:

    reasoner = TrendReasoner()

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
    )

    evidence = reasoner.evaluate(context)

    assert evidence == []