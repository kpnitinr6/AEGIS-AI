"""
AEGIS AI Domain

Immutable risk assessment.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class RiskAssessment:
    """
    Represents the outcome of evaluating
    whether a trade is permitted.
    """

    approved: bool
    reason: str