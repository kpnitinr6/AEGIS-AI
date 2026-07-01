"""
Tests for the TradeIntent domain model.
"""

from decimal import Decimal

from backend.domain import (
    Evidence,
    EvidenceDirection,
    EvidenceSource,
    Instrument,
    Timeframe,
)
from backend.domain.decision import (
    Decision,
    DecisionAction,
)
from backend.domain.trade_intent import TradeIntent


def make_instrument() -> Instrument:
    return Instrument(
        code="XAUUSD",
        name="Gold Spot",
    )


def make_decision() -> Decision:
    return Decision(
        action=DecisionAction.BUY,
        confidence=Decimal("1.00"),
        evidence=[
            Evidence(
                source=EvidenceSource.STRUCTURE,
                direction=EvidenceDirection.BULLISH,
                reason="Bullish structure.",
            )
        ],
    )


def test_trade_intent_contains_decision() -> None:

    decision = make_decision()

    intent = TradeIntent(
        decision=decision,
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
    )

    assert intent.decision == decision
    assert intent.instrument.code == "XAUUSD"
    assert intent.timeframe == Timeframe.M5


def test_trade_intent_exposes_decision_action() -> None:

    intent = TradeIntent(
        decision=make_decision(),
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
    )

    assert intent.decision.action == DecisionAction.BUY


def test_trade_intent_preserves_confidence() -> None:

    decision = make_decision()

    intent = TradeIntent(
        decision=decision,
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
    )

    assert intent.decision.confidence == Decimal("1.00")


def test_trade_intent_preserves_evidence() -> None:

    decision = make_decision()

    intent = TradeIntent(
        decision=decision,
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
    )

    assert len(intent.decision.evidence) == 1
    assert (
        intent.decision.evidence[0].reason
        == "Bullish structure."
    )