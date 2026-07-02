"""
AEGIS AI

Perception Pipeline.

Coordinates perception detectors and produces a
single immutable PerceptionResult from raw market
data.
"""

from __future__ import annotations

from backend.domain import CandleSeries
from backend.perception.perception_result import (
    PerceptionResult,
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

    Version 1

    Pipeline:

        CandleSeries
            ↓
        SwingDetector
            ↓
        StructureDetector
            ↓
        PerceptionResult

    Future versions will extend the pipeline with:

    - Break Of Structure
    - Change Of Character
    - Liquidity Sweep
    - Order Block
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

    def detect(
        self,
        candle_series: CandleSeries,
    ) -> PerceptionResult:

        if not isinstance(
            candle_series,
            CandleSeries,
        ):
            raise TypeError(
                "candle_series must be a CandleSeries"
            )

        swings = self._swing_detector.detect(
            candle_series,
        )

        if not swings:
            return PerceptionResult()

        market_structure = (
            self._structure_detector.detect(
                swings,
            )
        )

        return PerceptionResult(
            swings=swings,
            market_structure=market_structure,
        )