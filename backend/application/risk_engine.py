"""
AEGIS AI

Risk Engine.

Evaluates whether a trading decision
is permitted to proceed.
"""

from __future__ import annotations

from decimal import Decimal

from backend.domain import (
    Decision,
    RiskAssessment,
)
from backend.domain.decision import DecisionAction


class RiskEngine:
    """
    Version 2 risk engine.

    Rules

    1. NO_TRADE decisions are rejected.

    2. Decision confidence must meet
       the minimum confidence threshold.
    """

    MINIMUM_CONFIDENCE = Decimal("0.70")

    def evaluate(
        self,
        decision: Decision,
    ) -> RiskAssessment:

        if decision.action == DecisionAction.NO_TRADE:
            return RiskAssessment(
                approved=False,
                reason="Decision does not permit trading.",
            )

        if (
            decision.confidence
            < self.MINIMUM_CONFIDENCE
        ):
            return RiskAssessment(
                approved=False,
                reason=(
                    "Decision confidence below minimum threshold."
                ),
            )

        return RiskAssessment(
            approved=True,
            reason="Risk accepted.",
        )