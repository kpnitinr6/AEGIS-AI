"""
Tests for the Reasoner protocol.
"""

from datetime import datetime, timezone
from decimal import Decimal

from backend.domain import (
    Candle,
    Evidence,
    EvidenceDirection,
    EvidenceSource,
    Instrument,
    MarketContext,
    Price,
    Time,
    Timeframe,
)
from backend.reasoning.reasoner import Reasoner


def make_instrument() -> Instrument:
    return Instrument(
        code="XAUUSD",
        name="Gold Spot",
    )


def make_price() -> Price:
    return Price(
        instrument=make_instrument(),
        amount=Decimal("3350"),
        time=Time(
            datetime(
                2026,
                7,
                2,
                9,
                0,
                tzinfo=timezone.utc,
            )
        ),
    )


def make_evidence() -> Evidence:

    return Evidence(
        source=EvidenceSource.TREND,
        direction=EvidenceDirection.BULLISH,
        reason="Dummy reasoning evidence.",
    )


class DummyReasoner:
    def evaluate(
        self,
        context: MarketContext,
    ) -> list[Evidence]:
        return [make_evidence()]


def test_dummy_reasoner_implements_protocol() -> None:

    reasoner: Reasoner = DummyReasoner()

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
    )

    evidence = reasoner.evaluate(context)

    assert len(evidence) == 1
    assert evidence[0].direction == EvidenceDirection.BULLISH