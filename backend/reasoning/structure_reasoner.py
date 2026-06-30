"""
AEGIS AI

Structure Reasoner.

Transforms the latest confirmed market structure into
explainable evidence.
"""

from __future__ import annotations

from backend.domain import (
    Evidence,
    EvidenceDirection,
    EvidenceSource,
    MarketContext,
    StructureType,
)

from backend.reasoning.reasoner import Reasoner


class StructureReasoner(Reasoner):
    """
    Produces evidence from the latest confirmed
    market structure.
    """

    def evaluate(
        self,
        context: MarketContext,
    ) -> list[Evidence]:

        if context.market_structure is None:
            return []

        if len(context.market_structure) == 0:
            return []

        latest = context.market_structure.latest()

        assert latest is not None

        if latest.structure == StructureType.HIGHER_HIGH:
            return [
                Evidence(
                    source=EvidenceSource.STRUCTURE,
                    direction=EvidenceDirection.BULLISH,
                    reason=(
                        "Latest confirmed structure is a Higher High."
                    ),
                )
            ]

        if latest.structure == StructureType.HIGHER_LOW:
            return [
                Evidence(
                    source=EvidenceSource.STRUCTURE,
                    direction=EvidenceDirection.BULLISH,
                    reason=(
                        "Latest confirmed structure is a Higher Low."
                    ),
                )
            ]

        if latest.structure == StructureType.LOWER_HIGH:
            return [
                Evidence(
                    source=EvidenceSource.STRUCTURE,
                    direction=EvidenceDirection.BEARISH,
                    reason=(
                        "Latest confirmed structure is a Lower High."
                    ),
                )
            ]

        if latest.structure == StructureType.LOWER_LOW:
            return [
                Evidence(
                    source=EvidenceSource.STRUCTURE,
                    direction=EvidenceDirection.BEARISH,
                    reason=(
                        "Latest confirmed structure is a Lower Low."
                    ),
                )
            ]

        return []