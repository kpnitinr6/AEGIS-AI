"""
Tests for the MajorityVotePolicy.
"""

from decimal import Decimal

from backend.domain.policies.majority_vote_policy import (
    MajorityVotePolicy,
)
from backend.domain import (
    Evidence,
    EvidenceDirection,
    EvidenceSource,
)
from backend.domain.decision import (
    Decision,
    DecisionAction,
)


def bullish() -> Evidence:
    return Evidence(
        source=EvidenceSource.STRUCTURE,
        direction=EvidenceDirection.BULLISH,
        reason="Bullish evidence.",
    )


def bearish() -> Evidence:
    return Evidence(
        source=EvidenceSource.STRUCTURE,
        direction=EvidenceDirection.BEARISH,
        reason="Bearish evidence.",
    )


def test_all_bullish_returns_buy() -> None:

    policy = MajorityVotePolicy()

    decision = policy.decide(
        [
            bullish(),
            bullish(),
            bullish(),
        ]
    )

    assert isinstance(
        decision,
        Decision,
    )

    assert decision.action == DecisionAction.BUY
    assert decision.confidence == Decimal("1.00")
    assert len(decision.evidence) == 3


def test_all_bearish_returns_sell() -> None:

    policy = MajorityVotePolicy()

    decision = policy.decide(
        [
            bearish(),
            bearish(),
            bearish(),
        ]
    )

    assert decision.action == DecisionAction.SELL
    assert decision.confidence == Decimal("1.00")


def test_majority_bullish_returns_buy() -> None:

    policy = MajorityVotePolicy()

    decision = policy.decide(
        [
            bullish(),
            bullish(),
            bearish(),
        ]
    )

    assert decision.action == DecisionAction.BUY
    assert decision.confidence == Decimal("0.67")


def test_majority_bearish_returns_sell() -> None:

    policy = MajorityVotePolicy()

    decision = policy.decide(
        [
            bearish(),
            bearish(),
            bullish(),
        ]
    )

    assert decision.action == DecisionAction.SELL
    assert decision.confidence == Decimal("0.67")


def test_equal_votes_returns_no_trade() -> None:

    policy = MajorityVotePolicy()

    decision = policy.decide(
        [
            bullish(),
            bearish(),
        ]
    )

    assert decision.action == DecisionAction.NO_TRADE
    assert decision.confidence == Decimal("0.50")


def test_no_evidence_returns_no_trade() -> None:

    policy = MajorityVotePolicy()

    decision = policy.decide([])

    assert decision.action == DecisionAction.NO_TRADE
    assert decision.confidence == Decimal("0.00")
    assert decision.evidence == []