"""
AEGIS AI Reasoning

Defines the contract for all reasoning components.
"""

from __future__ import annotations

from typing import Protocol

from backend.domain.evidence import Evidence
from backend.domain.market_context import MarketContext


class Reasoner(Protocol):
    """
    Contract implemented by every reasoning component.

    A reasoner examines the current MarketContext and
    produces zero or more Evidence objects.

    Reasoners never execute trades and never modify
    MarketContext.
    """

    def evaluate(
        self,
        context: MarketContext,
    ) -> list[Evidence]:
        """
        Evaluate the supplied market context.

        Returns:
            A list of Evidence objects produced by this
            reasoning component.
        """
        ...
    