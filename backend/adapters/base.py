"""
AEGIS AI

Market Adapter Contract
"""

from abc import ABC, abstractmethod

from backend.domain.candle_series import CandleSeries
from backend.domain.timeframe import Timeframe


class MarketAdapter(ABC):
    """
    Every market data provider must implement
    this interface.
    """

    @abstractmethod
    def get_candles(
        self,
        symbol: str,
        timeframe: Timeframe,
        count: int,
    ) -> CandleSeries:
        """
        Return market candles.
        """
        raise NotImplementedError