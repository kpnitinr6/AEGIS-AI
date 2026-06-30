"""
Tests for the RiskEngine.
"""

from decimal import Decimal

from backend.application.risk_engine import RiskEngine
from backend.domain import (
    Decision,
    Evidence,
    EvidenceDirection,
    EvidenceSource,
    RiskAssessment,
)
from backend.domain.decision import DecisionAction


def make_evidence() -> list[Evidence]:
    return [
        Evidence(
            source=EvidenceSource.STRUCTURE,
            direction=EvidenceDirection.BULLISH,
            reason="Bullish structure.",
        )
    ]


def make_decision(
    action: DecisionAction,
    confidence: str,
) -> Decision:
    return Decision(
        action=action,
        confidence=Decimal(confidence),
        evidence=make_evidence(),
    )


def test_buy_with_high_confidence_is_approved() -> None:

    engine = RiskEngine()

    assessment = engine.evaluate(
        make_decision(
            DecisionAction.BUY,
            "1.00",
        )
    )

    assert isinstance(
        assessment,
        RiskAssessment,
    )

    assert assessment.approved is True
    assert assessment.reason == "Risk accepted."


def test_sell_with_high_confidence_is_approved() -> None:

    engine = RiskEngine()

    assessment = engine.evaluate(
        make_decision(
            DecisionAction.SELL,
            "0.85",
        )
    )

    assert assessment.approved is True
    assert assessment.reason == "Risk accepted."


def test_low_confidence_trade_is_rejected() -> None:

    engine = RiskEngine()

    assessment = engine.evaluate(
        make_decision(
            DecisionAction.BUY,
            "0.69",
        )
    )

    assert assessment.approved is False

    assert (
        assessment.reason
        == "Decision confidence below minimum threshold."
    )


def test_no_trade_is_rejected() -> None:

    engine = RiskEngine()

    assessment = engine.evaluate(
        make_decision(
            DecisionAction.NO_TRADE,
            "0.00",
        )
    )

    assert assessment.approved is False

    assert (
        assessment.reason
        == "Decision does not permit trading."
    )