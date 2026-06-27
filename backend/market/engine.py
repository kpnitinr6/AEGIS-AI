"""
AEGIS AI

Market Engine
"""

from backend.adapters.base import MarketAdapter
from backend.domain.candle_series import CandleSeries
from backend.domain.timeframe import Timeframe


class MarketEngine:
    """
    Central gateway for market data.
    """

    def __init__(self, adapter: MarketAdapter) -> None:
        self._adapter = adapter

    def get_candles(
        self,
        symbol: str,
        timeframe: Timeframe,
        count: int,
    ) -> CandleSeries:

        return self._adapter.get_candles(
            symbol=symbol,
            timeframe=timeframe,
            count=count,
        )