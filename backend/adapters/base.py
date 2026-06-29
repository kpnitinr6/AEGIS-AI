"""
AEGIS AI

Market Adapter Contract
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from backend.domain.candle_series import CandleSeries
from backend.domain.instrument import Instrument
from backend.domain.timeframe import Timeframe


class MarketAdapter(ABC):
    """
    Contract implemented by every market data provider.

    Adapters retrieve market data from external systems
    and convert it into AEGIS domain objects.
    """

    @abstractmethod
    def get_candles(
        self,
        instrument: Instrument,
        timeframe: Timeframe,
        count: int,
    ) -> CandleSeries:
        """
        Retrieve completed candles.
        """
        raise NotImplementedError