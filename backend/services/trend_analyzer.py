"""
AEGIS AI Services

Derives the current market trend from MarketStructure.
"""

from __future__ import annotations

from backend.domain.market_structure import MarketStructure
from backend.domain.structure_type import StructureType
from backend.domain.trend import Trend
from backend.domain.trend_state import TrendState

from backend.services.analyzer import Analyzer


class TrendAnalyzer(Analyzer):
    """
    Analyzes market structure to determine trend.

    Version 1:

    HH -> Bullish +1
    HL -> Bullish +1

    LH -> Bearish +1
    LL -> Bearish +1

    BOS, CHOCH and RANGE are ignored for now.
    """

    def analyze(self, subject: MarketStructure) -> Trend:

        if not isinstance(subject, MarketStructure):
            raise TypeError(
                "subject must be a MarketStructure"
            )

        bullish = 0
        bearish = 0

        for point in subject.structure_points:

            if point.structure in (
                StructureType.HIGHER_HIGH,
                StructureType.HIGHER_LOW,
            ):
                bullish += 1

            elif point.structure in (
                StructureType.LOWER_HIGH,
                StructureType.LOWER_LOW,
            ):
                bearish += 1

        if len(subject) == 0:
            state = TrendState.UNKNOWN

        elif bullish > bearish:
            state = TrendState.BULLISH

        elif bearish > bullish:
            state = TrendState.BEARISH

        else:
            state = TrendState.SIDEWAYS

        return Trend(
            state=state,
            market_structure=subject,
        )