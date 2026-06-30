"""
AEGIS AI

Market Analyzer.

Transforms raw market data into a MarketContext.
"""

from __future__ import annotations

from backend.domain import (
    Candle,
    MarketContext,
)


class MarketAnalyzer:
    """
    Builds a MarketContext from raw market data.

    Version 1:
    - Uses the first candle to establish the instrument
      and timeframe.
    - Leaves all derived market understanding empty.
    """

    def analyze(
        self,
        candles: list[Candle],
    ) -> MarketContext:

        if not candles:
            raise ValueError(
                "candles must not be empty"
            )

        first = candles[0]

        return MarketContext(
            instrument=first.instrument,
            timeframe=first.timeframe,
        )