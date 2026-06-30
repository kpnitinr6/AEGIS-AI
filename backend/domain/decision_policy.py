"""
AEGIS AI Domain

Decision Policy.

Defines the contract for converting market evidence
into a trading Decision.
"""

from __future__ import annotations

from typing import Protocol

from backend.domain.decision import Decision
from backend.domain.evidence import Evidence


class DecisionPolicy(Protocol):
    """
    Contract implemented by every decision policy.

    A decision policy receives all available evidence
    and produces a single immutable Decision.
    """

    def decide(
        self,
        evidence: list[Evidence],
    ) -> Decision:
        """
        Produce a trading decision from evidence.
        """
        ...