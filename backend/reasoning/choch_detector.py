"""
AEGIS AI

Change of Character (CHoCH) Detector.

Interprets a confirmed MarketStructure and produces
explainable market evidence.
"""

from __future__ import annotations

from backend.domain import (
    Evidence,
    EvidenceDirection,
    EvidenceSource,
    MarketStructure,
    StructureType,
)


class CHOCHDetector:
    """
    Detect a confirmed Change of Character.

    Version 1 (Dow Theory)

    Bullish CHoCH

        Lower Low
            ↓
        Higher High

    Bearish CHoCH

        Higher High
            ↓
        Lower Low
    """

    def detect(
        self,
        market_structure: MarketStructure,
    ) -> Evidence | None:

        if not isinstance(
            market_structure,
            MarketStructure,
        ):
            raise TypeError(
                "market_structure must be a MarketStructure"
            )

        if len(market_structure) < 2:
            return None

        previous = market_structure.previous()
        latest = market_structure.latest()

        assert previous is not None
        assert latest is not None

        bullish = (
            previous.structure == StructureType.LOWER_LOW
            and latest.structure == StructureType.HIGHER_HIGH
        )

        if bullish:
            return Evidence(
                source=EvidenceSource.CHANGE_OF_CHARACTER,
                direction=EvidenceDirection.BULLISH,
                reason=(
                    "Confirmed bullish change of character."
                ),
            )

        bearish = (
            previous.structure == StructureType.HIGHER_HIGH
            and latest.structure == StructureType.LOWER_LOW
        )

        if bearish:
            return Evidence(
                source=EvidenceSource.CHANGE_OF_CHARACTER,
                direction=EvidenceDirection.BEARISH,
                reason=(
                    "Confirmed bearish change of character."
                ),
            )

        return None