"""
AEGIS AI

Break of Structure (BOS) Detector.

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


class BOSDetector:
    """
    Detect Break of Structure (BOS).

    Version 1

    Bullish BOS:
        Last two structure points are
        Higher High -> Higher Low

    Bearish BOS:
        Last two structure points are
        Lower High -> Lower Low
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
            previous.structure == StructureType.HIGHER_HIGH
            and latest.structure == StructureType.HIGHER_LOW
        )

        if bullish:
            return Evidence(
                source=EvidenceSource.BREAK_OF_STRUCTURE,
                direction=EvidenceDirection.BULLISH,
                reason=(
                    "Confirmed bullish break of structure."
                ),
            )

        bearish = (
            previous.structure == StructureType.LOWER_HIGH
            and latest.structure == StructureType.LOWER_LOW
        )

        if bearish:
            return Evidence(
                source=EvidenceSource.BREAK_OF_STRUCTURE,
                direction=EvidenceDirection.BEARISH,
                reason=(
                    "Confirmed bearish break of structure."
                ),
            )

        return None