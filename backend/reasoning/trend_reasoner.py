"""
AEGIS AI Reasoning

Produces evidence from the current market trend.
"""

from __future__ import annotations

from backend.domain import (
    Evidence,
    EvidenceDirection,
    EvidenceSource,
    MarketContext,
    TrendState,
)
from backend.reasoning.reasoner import Reasoner


class TrendReasoner(Reasoner):
    """
    Produces evidence from a confirmed market trend.
    """

    def evaluate(
        self,
        context: MarketContext,
    ) -> list[Evidence]:
        """
        Evaluate the supplied market context and produce
        evidence based on the confirmed market trend.
        """

        if context.trend is None:
            return []

        if context.trend.state == TrendState.BULLISH:
            return [
                Evidence(
                    source=EvidenceSource.TREND,
                    direction=EvidenceDirection.BULLISH,
                    reason="Confirmed bullish trend.",
                )
            ]

        if context.trend.state == TrendState.BEARISH:
            return [
                Evidence(
                    source=EvidenceSource.TREND,
                    direction=EvidenceDirection.BEARISH,
                    reason="Confirmed bearish trend.",
                )
            ]

        if context.trend.state == TrendState.SIDEWAYS:
            return [
                Evidence(
                    source=EvidenceSource.TREND,
                    direction=EvidenceDirection.NEUTRAL,
                    reason="Market is moving sideways.",
                )
            ]

        return [
            Evidence(
                source=EvidenceSource.TREND,
                direction=EvidenceDirection.NEUTRAL,
                reason="Market trend is unknown.",
            )
        ]