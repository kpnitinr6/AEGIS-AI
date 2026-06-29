"""
AEGIS AI Domain

Represents the current market trend.
"""

from __future__ import annotations

from dataclasses import dataclass

from backend.domain.market_structure import MarketStructure
from backend.domain.trend_state import TrendState


@dataclass(frozen=True, slots=True)
class Trend:
    """
    Immutable value object representing the current market trend.

    A Trend is derived from MarketStructure by an analyzer.
    The Trend itself contains no analysis logic.
    """

    state: TrendState
    market_structure: MarketStructure

    def __post_init__(self) -> None:
        if not isinstance(self.state, TrendState):
            raise TypeError("state must be a TrendState")

        if not isinstance(self.market_structure, MarketStructure):
            raise TypeError(
                "market_structure must be a MarketStructure"
            )