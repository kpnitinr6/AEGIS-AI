"""
AEGIS AI

Perception Pipeline.

Coordinates all perception detectors and produces
market facts from raw market data.
"""

from __future__ import annotations

from backend.domain import (
    CandleSeries,
    MarketStructure,
    Swing,
)
from backend.perception.structure_detector import (
    StructureDetector,
)
from backend.perception.swing_detector import (
    SwingDetector,
)


class PerceptionPipeline:
    """
    Coordinates the perception layer.

    Responsibilities
    ----------------
    - Detect swings.
    - Detect market structure.

    Future versions will also detect:
    - Break of Structure
    - Change of Character
    - Liquidity Sweeps
    - Order Blocks
    - Fair Value Gaps
    """

    def __init__(
        self,
        swing_detector: SwingDetector | None = None,
        structure_detector: StructureDetector | None = None,
    ) -> None:

        self._swing_detector = (
            swing_detector
            if swing_detector is not None
            else SwingDetector()
        )

        self._structure_detector = (
            structure_detector
            if structure_detector is not None
            else StructureDetector()
        )

    def detect_swings(
        self,
        candle_series: CandleSeries,
    ) -> list[Swing]:

        return self._swing_detector.detect(
            candle_series,
        )

    def detect_market_structure(
        self,
        swings: list[Swing],
    ) -> MarketStructure:

        return self._structure_detector.detect(
            swings,
        )