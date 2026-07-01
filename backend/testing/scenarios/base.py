"""
AEGIS AI Testing

Market Scenario contract.

A MarketScenario produces a deterministic CandleSeries
used for integration and end-to-end testing.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from backend.domain import (
    CandleSeries,
    Instrument,
    Timeframe,
)


class MarketScenario(ABC):
    """
    Base class for deterministic market scenarios.

    A scenario is responsible only for generating
    a CandleSeries representing a known market
    condition.

    Examples
    --------
    - Bullish Trend
    - Bearish Trend
    - Sideways Range
    - Liquidity Sweep
    - Break of Structure
    """

    @abstractmethod
    def generate(
        self,
        instrument: Instrument,
        timeframe: Timeframe,
        count: int,
    ) -> CandleSeries:
        """
        Generate a deterministic CandleSeries.
        """
        raise NotImplementedError