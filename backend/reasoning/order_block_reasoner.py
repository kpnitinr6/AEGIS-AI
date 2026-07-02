"""
AEGIS AI

Order Block Reasoner.

Transforms the latest confirmed Order Block
into explainable evidence.
"""

from __future__ import annotations

from backend.domain import (
    Evidence,
    EvidenceDirection,
    EvidenceSource,
    MarketContext,
    OrderBlockDirection,
)

from backend.reasoning.reasoner import Reasoner


class OrderBlockReasoner(Reasoner):
    """
    Produces evidence from the latest confirmed
    Order Block.
    """

    def evaluate(
        self,
        context: MarketContext,
    ) -> list[Evidence]:

        if not context.order_blocks:
            return []

        latest = context.order_blocks[-1]

        if (
            latest.direction
            == OrderBlockDirection.BULLISH
        ):
            return [
                Evidence(
                    source=EvidenceSource.ORDER_BLOCK,
                    direction=EvidenceDirection.BULLISH,
                    reason=(
                        "Confirmed bullish Order Block."
                    ),
                )
            ]

        return [
            Evidence(
                source=EvidenceSource.ORDER_BLOCK,
                direction=EvidenceDirection.BEARISH,
                reason=(
                    "Confirmed bearish Order Block."
                ),
            )
        ]