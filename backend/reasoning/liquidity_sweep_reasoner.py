"""
AEGIS AI

Liquidity Sweep Reasoner.

Produces explainable evidence from confirmed
liquidity sweep events.
"""

from __future__ import annotations

from backend.domain import (
    Evidence,
    EvidenceDirection,
    EvidenceSource,
    LiquiditySweepDirection,
    MarketContext,
)

from backend.reasoning.reasoner import Reasoner


class LiquiditySweepReasoner(Reasoner):
    """
    Produces evidence from the latest confirmed
    liquidity sweep.
    """

    def evaluate(
        self,
        context: MarketContext,
    ) -> list[Evidence]:

        if not context.liquidity_sweeps:
            return []

        latest = context.liquidity_sweeps[-1]

        if (
            latest.direction
            == LiquiditySweepDirection.BULLISH
        ):
            return [
                Evidence(
                    source=EvidenceSource.LIQUIDITY_SWEEP,
                    direction=EvidenceDirection.BULLISH,
                    reason=(
                        "Confirmed bullish liquidity sweep."
                    ),
                )
            ]

        if (
            latest.direction
            == LiquiditySweepDirection.BEARISH
        ):
            return [
                Evidence(
                    source=EvidenceSource.LIQUIDITY_SWEEP,
                    direction=EvidenceDirection.BEARISH,
                    reason=(
                        "Confirmed bearish liquidity sweep."
                    ),
                )
            ]

        return []