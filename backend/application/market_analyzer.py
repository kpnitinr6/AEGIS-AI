"""
AEGIS AI

Market Analyzer.

Transforms raw market data into a MarketContext.
"""

from __future__ import annotations

from backend.services.trend_analyzer import TrendAnalyzer

from backend.domain import (
    CandleSeries,
    MarketContext,
)
from backend.perception import (
    StructureDetector,
    SwingDetector,
)


class MarketAnalyzer:
    """
    Builds a MarketContext from raw market data.

    Responsibilities:
    - Validate input.
    - Detect swings.
    - Detect market structure.
    - Analyze trend.
    - Assemble a MarketContext.
    """

    def __init__(
        self,
        swing_detector: SwingDetector | None = None,
        structure_detector: StructureDetector | None = None,
        trend_analyzer: TrendAnalyzer | None = None,
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

        self._trend_analyzer = (
            trend_analyzer
            if trend_analyzer is not None
            else TrendAnalyzer()
        )

    def analyze(
        self,
        candle_series: CandleSeries,
    ) -> MarketContext:

        if len(candle_series) < 2:
            raise ValueError(
                "at least two candles are required"
            )

        swings = self._swing_detector.detect(
            candle_series,
        )

        market_structure = None
        trend = None

        if swings:
            market_structure = (
                self._structure_detector.detect(
                    swings,
                )
            )

            trend = self._trend_analyzer.analyze(
                market_structure,
            )

        first = candle_series.first()

        return MarketContext(
            instrument=first.instrument,
            timeframe=first.timeframe,
            market_structure=market_structure,
            trend=trend,
        )