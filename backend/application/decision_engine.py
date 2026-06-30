"""
AEGIS AI

Decision Engine.

Coordinates registered reasoning components and
delegates the final decision to a DecisionPolicy.
"""

from __future__ import annotations

from backend.domain import (
    Decision,
    Evidence,
    MarketContext,
)
from backend.domain.decision_policy import DecisionPolicy
from backend.reasoning.reasoner import Reasoner


class DecisionEngine:
    """
    Coordinates all registered reasoners.

    Version 2

    - Collects evidence from reasoners.
    - Delegates decision making to a DecisionPolicy.
    """

    def __init__(
        self,
        reasoners: list[Reasoner],
        policy: DecisionPolicy,
    ) -> None:
        self._reasoners = reasoners
        self._policy = policy

    def decide(
        self,
        context: MarketContext,
    ) -> Decision:

        evidence: list[Evidence] = []

        for reasoner in self._reasoners:
            evidence.extend(
                reasoner.evaluate(context)
            )

        return self._policy.decide(
            evidence,
        )