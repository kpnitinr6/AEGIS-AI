"""
AEGIS AI Domain

Immutable trading decision.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from enum import Enum, auto

from backend.domain.evidence import Evidence


class DecisionAction(Enum):
    """
    Possible actions produced by the Decision Engine.
    """

    BUY = auto()
    SELL = auto()
    HOLD = auto()
    NO_TRADE = auto()


@dataclass(frozen=True, slots=True)
class Decision:
    """
    Immutable trading decision.

    Attributes
    ----------
    action
        The action recommended by the Decision Engine.

    confidence
        Confidence score between 0.00 and 1.00.

    evidence
        Evidence supporting the decision.
    """

    action: DecisionAction
    confidence: Decimal
    evidence: list[Evidence]