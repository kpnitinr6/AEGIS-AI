"""
AEGIS AI

Market Shift Detector.

Combines lower-level structural evidence into a single
Market Shift evidence.

A market shift is confirmed when either:

- A Change of Character (CHoCH) occurs.
- A Break of Structure (BOS) confirms continuation.

Version 1 keeps this detector intentionally simple and
fully explainable.
"""

from __future__ import annotations

from backend.domain import (
    Evidence,
    MarketStructure,
)

from backend.reasoning.bos_detector import BOSDetector
from backend.reasoning.choch_detector import CHOCHDetector


class MarketShiftDetector:
    """
    Detect significant market shifts.

    Priority:

    1. CHoCH
    2. BOS
    """

    def __init__(self) -> None:
        self._bos = BOSDetector()
        self._choch = CHOCHDetector()

    def detect(
        self,
        market_structure: MarketStructure,
    ) -> Evidence | None:

        choch = self._choch.detect(
            market_structure,
        )

        if choch is not None:
            return choch

        bos = self._bos.detect(
            market_structure,
        )

        if bos is not None:
            return bos

        return None