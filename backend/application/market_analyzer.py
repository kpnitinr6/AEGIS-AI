"""
AEGIS AI

Market Analyzer.

Transforms raw market data into a MarketContext.
"""

from __future__ import annotations
from backend.services.trend_analyzer import TrendAnalyzer

from backend.domain import (
    Candle,
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

    Version 2

    Responsibilities:
    - Validate input.
    - Convert candles into a CandleSeries.
    - Detect swings.
    - Detect market structure.
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
        candles: list[Candle],
    ) -> MarketContext:

        if len(candles) < 2:
            raise ValueError(
                "at least two candles are required"
            )

        series = CandleSeries()

        for candle in candles:
            series.add(candle)

        swings = self._swing_detector.detect(
            series,
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

        first = candles[0]

        return MarketContext(
            instrument=first.instrument,
            timeframe=first.timeframe,
            market_structure=market_structure,
            trend=trend,
        )