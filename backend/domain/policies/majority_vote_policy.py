"""
AEGIS AI Domain

Majority Vote Decision Policy.
"""

from __future__ import annotations

from decimal import Decimal, ROUND_HALF_UP

from backend.domain.decision import (
    Decision,
    DecisionAction,
)
from backend.domain.decision_policy import DecisionPolicy
from backend.domain.evidence import (
    Evidence,
    EvidenceDirection,
)


class MajorityVotePolicy(DecisionPolicy):
    """
    Produce a Decision using simple majority voting.

    Version 1

    Every Evidence contributes one vote.
    """

    def decide(
        self,
        evidence: list[Evidence],
    ) -> Decision:

        if not evidence:
            return Decision(
                action=DecisionAction.NO_TRADE,
                confidence=Decimal("0.00"),
                evidence=[],
            )

        bullish = sum(
            1
            for item in evidence
            if item.direction == EvidenceDirection.BULLISH
        )

        bearish = sum(
            1
            for item in evidence
            if item.direction == EvidenceDirection.BEARISH
        )

        total = bullish + bearish

        if bullish > bearish:
            action = DecisionAction.BUY
            winning_votes = bullish

        elif bearish > bullish:
            action = DecisionAction.SELL
            winning_votes = bearish

        else:
            action = DecisionAction.NO_TRADE
            winning_votes = bullish

        confidence = (
            Decimal(winning_votes)
            / Decimal(total)
        ).quantize(
            Decimal("0.01"),
            rounding=ROUND_HALF_UP,
        )

        return Decision(
            action=action,
            confidence=confidence,
            evidence=evidence,
        )