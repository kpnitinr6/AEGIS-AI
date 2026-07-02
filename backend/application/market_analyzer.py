"""
AEGIS AI

Market Analyzer.

Transforms raw market data into a MarketContext.
"""

from __future__ import annotations

from backend.domain import (
    CandleSeries,
    MarketContext,
)
from backend.perception import (
    PerceptionPipeline,
)
from backend.services.trend_analyzer import (
    TrendAnalyzer,
)


class MarketAnalyzer:
    """
    Builds a MarketContext from raw market data.

    Responsibilities
    ----------------
    - Validate input.
    - Delegate perception to the PerceptionPipeline.
    - Analyze trend.
    - Assemble a MarketContext.
    """

    def __init__(
        self,
        perception_pipeline: PerceptionPipeline | None = None,
        trend_analyzer: TrendAnalyzer | None = None,
    ) -> None:

        self._perception_pipeline = (
            perception_pipeline
            if perception_pipeline is not None
            else PerceptionPipeline()
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

        perception = (
            self._perception_pipeline.detect(
                candle_series,
            )
        )

        trend = None

        if perception.market_structure is not None:
            trend = self._trend_analyzer.analyze(
                perception.market_structure,
            )

        first = candle_series.first()

        return MarketContext(
            instrument=first.instrument,
            timeframe=first.timeframe,
            market_structure=perception.market_structure,
            trend=trend,
            break_of_structures=(
                perception.break_of_structures
            ),
            change_of_characters=(
                perception.change_of_characters
            ),
            liquidity_sweeps=(
                perception.liquidity_sweeps
            ),
            order_blocks=(
                perception.order_blocks
            ),
        )