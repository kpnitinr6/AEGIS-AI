"""
AEGIS AI

Weighted Decision Policy.
"""

from __future__ import annotations

from decimal import Decimal

from backend.domain import (
    Decision,
    Evidence,
    EvidenceDirection,
    EvidenceSource,
)
from backend.domain.decision import (
    DecisionAction,
)
from backend.domain.decision_policy import (
    DecisionPolicy,
)


class WeightedDecisionPolicy(DecisionPolicy):
    """
    Produces a decision by applying configurable
    weights to market evidence.
    """

    _WEIGHTS = {
        EvidenceSource.TREND: Decimal("0.30"),
        EvidenceSource.STRUCTURE: Decimal("0.20"),
        EvidenceSource.BREAK_OF_STRUCTURE: Decimal("0.20"),
        EvidenceSource.LIQUIDITY_SWEEP: Decimal("0.20"),
        EvidenceSource.CHANGE_OF_CHARACTER: Decimal("0.30"),
    }

    _BUY_THRESHOLD = Decimal("0.20")
    _SELL_THRESHOLD = Decimal("-0.20")

    def decide(
        self,
        evidence: list[Evidence],
    ) -> Decision:

        score = Decimal("0.00")

        for item in evidence:

            weight = self._WEIGHTS.get(
                item.source,
                Decimal("0.10"),
            )

            if (
                item.direction
                == EvidenceDirection.BULLISH
            ):
                score += weight

            else:
                score -= weight

        if score > self._BUY_THRESHOLD:
            action = DecisionAction.BUY

        elif score < self._SELL_THRESHOLD:
            action = DecisionAction.SELL

        else:
            action = DecisionAction.HOLD

        confidence = min(
            abs(score),
            Decimal("1.00"),
        )

        return Decision(
            action=action,
            confidence=confidence.quantize(
                Decimal("0.01")
            ),
            evidence=evidence,
        )