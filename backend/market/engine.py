"""
AEGIS AI

Market Engine
"""

from __future__ import annotations

from backend.adapters.base import MarketAdapter
from backend.domain.candle_series import CandleSeries
from backend.domain.instrument import Instrument
from backend.domain.timeframe import Timeframe


class MarketEngine:
    """
    Central gateway for market data.

    The engine orchestrates retrieval of market data
    without knowing anything about the underlying
    provider implementation.
    """

    def __init__(self, adapter: MarketAdapter) -> None:
        self._adapter = adapter

    def get_candles(
        self,
        instrument: Instrument,
        timeframe: Timeframe,
        count: int,
    ) -> CandleSeries:

        return self._adapter.get_candles(
            instrument=instrument,
            timeframe=timeframe,
            count=count,
        )