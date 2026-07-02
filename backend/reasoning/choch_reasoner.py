"""
AEGIS AI

Change Of Character Reasoner.

Produces evidence from confirmed
Change Of Character events.
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


class CHOCHReasoner(Reasoner):
    """
    Produces evidence from the latest confirmed
    Change Of Character event.
    """

    def evaluate(
        self,
        context: MarketContext,
    ) -> list[Evidence]:

        if not context.change_of_characters:
            return []

        latest = context.change_of_characters[-1]

        structure = latest.broken_structure.structure

        if structure == StructureType.LOWER_LOW:
            return [
                Evidence(
                    source=EvidenceSource.CHANGE_OF_CHARACTER,
                    direction=EvidenceDirection.BULLISH,
                    reason=(
                        "Confirmed bullish change of character."
                    ),
                )
            ]

        if structure == StructureType.HIGHER_HIGH:
            return [
                Evidence(
                    source=EvidenceSource.CHANGE_OF_CHARACTER,
                    direction=EvidenceDirection.BEARISH,
                    reason=(
                        "Confirmed bearish change of character."
                    ),
                )
            ]

        return []