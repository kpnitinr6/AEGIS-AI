"""
AEGIS AI Understanding

Builds a MarketContext from confirmed market facts.
"""

from __future__ import annotations

from backend.domain.instrument import Instrument
from backend.domain.market_context import MarketContext
from backend.domain.market_structure import MarketStructure
from backend.domain.timeframe import Timeframe
from backend.domain.trend import Trend


class MarketContextBuilder:
    """
    Builds a MarketContext from confirmed market facts.

    This class performs no reasoning and no market analysis.
    It simply assembles a coherent snapshot of the market.
    """

    def build(
        self,
        *,
        instrument: Instrument,
        timeframe: Timeframe,
        market_structure: MarketStructure | None = None,
        trend: Trend | None = None,
    ) -> MarketContext:

        return MarketContext(
            instrument=instrument,
            timeframe=timeframe,
            market_structure=market_structure,
            trend=trend,
        )