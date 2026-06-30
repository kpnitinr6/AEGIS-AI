"""
Tests for the DecisionEngine.
"""

from decimal import Decimal

from backend.application.decision_engine import DecisionEngine
from backend.domain.policies.majority_vote_policy import (
    MajorityVotePolicy,
)
from backend.domain import (
    Evidence,
    EvidenceDirection,
    EvidenceSource,
    Instrument,
    MarketContext,
    Timeframe,
)
from backend.domain.decision import (
    Decision,
    DecisionAction,
)


class BullishReasoner:
    """
    Fake reasoner used by the tests.
    """

    def evaluate(
        self,
        context: MarketContext,
    ) -> list[Evidence]:

        return [
            Evidence(
                source=EvidenceSource.STRUCTURE,
                direction=EvidenceDirection.BULLISH,
                reason="Bullish structure.",
            )
        ]


def make_context() -> MarketContext:

    return MarketContext(
        instrument=Instrument(
            code="XAUUSD",
            name="Gold Spot",
        ),
        timeframe=Timeframe.M5,
    )


def test_decision_engine_collects_evidence() -> None:
    engine = DecisionEngine(
        reasoners=[
            BullishReasoner(),
        ],
        policy=MajorityVotePolicy(),
    )
    decision = engine.decide(
        make_context(),
    )
    assert isinstance(
        decision,
        Decision,
    )

    assert decision.action == DecisionAction.BUY

    assert decision.confidence == Decimal("1.00")

    assert len(
        decision.evidence
    ) == 1

    assert (
        decision.evidence[0].reason
        == "Bullish structure."
    )