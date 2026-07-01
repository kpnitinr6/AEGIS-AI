"""
Tests for the TradeIntentFactory.
"""

from decimal import Decimal
from backend.application.trade_intent_factory import (
    TradeIntentFactory,
)
from backend.domain import (
    Decision,
    Evidence,
    EvidenceDirection,
    EvidenceSource,
    Instrument,
    MarketContext,
    RiskAssessment,
    Timeframe,
)
from backend.domain.decision import DecisionAction


def make_context() -> MarketContext:
    return MarketContext(
        instrument=Instrument(
            code="XAUUSD",
            name="Gold Spot",
        ),
        timeframe=Timeframe.M5,
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


def test_factory_creates_trade_intent() -> None:

    factory = TradeIntentFactory()

    intent = factory.create(
        context=make_context(),
        decision=make_decision(),
        assessment=RiskAssessment(
            approved=True,
            reason="Risk accepted.",
        ),
    )

    assert intent is not None
    assert intent.instrument.code == "XAUUSD"
    assert intent.timeframe == Timeframe.M5
    assert intent.decision.action == DecisionAction.BUY


def test_factory_returns_none_when_rejected() -> None:

    factory = TradeIntentFactory()

    intent = factory.create(
        context=make_context(),
        decision=make_decision(),
        assessment=RiskAssessment(
            approved=False,
            reason="Risk rejected.",
        ),
    )

    assert intent is None