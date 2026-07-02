"""
Tests for WeightedDecisionPolicy.
"""

from decimal import Decimal

from backend.domain import (
    Evidence,
    EvidenceDirection,
    EvidenceSource,
)
from backend.domain.decision import (
    DecisionAction,
)
from backend.domain.policies.weighted_decision_policy import (
    WeightedDecisionPolicy,
)


def test_buy_decision() -> None:

    policy = WeightedDecisionPolicy()

    decision = policy.decide(
        [
            Evidence(
                source=EvidenceSource.TREND,
                direction=EvidenceDirection.BULLISH,
                reason="Bullish trend.",
            ),
            Evidence(
                source=EvidenceSource.BREAK_OF_STRUCTURE,
                direction=EvidenceDirection.BULLISH,
                reason="Bullish BOS.",
            ),
        ]
    )

    assert decision.action == DecisionAction.BUY
    assert decision.confidence == Decimal("0.50")


def test_sell_decision() -> None:

    policy = WeightedDecisionPolicy()

    decision = policy.decide(
        [
            Evidence(
                source=EvidenceSource.CHANGE_OF_CHARACTER,
                direction=EvidenceDirection.BEARISH,
                reason="Bearish CHOCH.",
            ),
        ]
    )

    assert decision.action == DecisionAction.SELL
    assert decision.confidence == Decimal("0.30")


def test_hold_decision() -> None:

    policy = WeightedDecisionPolicy()

    decision = policy.decide(
        [
            Evidence(
                source=EvidenceSource.STRUCTURE,
                direction=EvidenceDirection.BULLISH,
                reason="Bullish structure.",
            ),
            Evidence(
                source=EvidenceSource.STRUCTURE,
                direction=EvidenceDirection.BEARISH,
                reason="Bearish structure.",
            ),
        ]
    )

    assert decision.action == DecisionAction.HOLD
    assert decision.confidence == Decimal("0.00")


def test_confidence_is_capped_at_one() -> None:

    policy = WeightedDecisionPolicy()

    evidence = []

    for _ in range(10):
        evidence.append(
            Evidence(
                source=EvidenceSource.TREND,
                direction=EvidenceDirection.BULLISH,
                reason="Bullish trend.",
            )
        )

    decision = policy.decide(
        evidence,
    )

    assert decision.action == DecisionAction.BUY
    assert decision.confidence == Decimal("1.00")


def test_decision_contains_original_evidence() -> None:

    policy = WeightedDecisionPolicy()

    evidence = [
        Evidence(
            source=EvidenceSource.TREND,
            direction=EvidenceDirection.BULLISH,
            reason="Bullish trend.",
        )
    ]

    decision = policy.decide(
        evidence,
    )

    assert decision.evidence == evidence