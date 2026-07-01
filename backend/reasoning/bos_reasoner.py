"""
AEGIS AI

Break Of Structure Reasoner.

Produces evidence from confirmed Break Of Structure events.
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


class BOSReasoner(Reasoner):
    """
    Produces evidence from the latest confirmed
    Break Of Structure event.
    """

    def evaluate(
        self,
        context: MarketContext,
    ) -> list[Evidence]:

        if not context.break_of_structures:
            return []

        latest = context.break_of_structures[-1]

        structure = latest.broken_structure.structure

        if structure in (
            StructureType.HIGHER_HIGH,
            StructureType.HIGHER_LOW,
        ):
            return [
                Evidence(
                    source=EvidenceSource.BREAK_OF_STRUCTURE,
                    direction=EvidenceDirection.BULLISH,
                    reason=(
                        "Confirmed bullish break of structure."
                    ),
                )
            ]

        if structure in (
            StructureType.LOWER_HIGH,
            StructureType.LOWER_LOW,
        ):
            return [
                Evidence(
                    source=EvidenceSource.BREAK_OF_STRUCTURE,
                    direction=EvidenceDirection.BEARISH,
                    reason=(
                        "Confirmed bearish break of structure."
                    ),
                )
            ]

        return []