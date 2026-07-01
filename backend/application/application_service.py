"""
AEGIS AI

Application Service.

Coordinates the market adapter and the AEGIS application.
"""

from __future__ import annotations

from backend.adapters.base import MarketAdapter
from backend.application.aegis import AEGIS
from backend.domain import (
    Instrument,
    ProcessResult,
    Timeframe,
)


class ApplicationService:
    """
    Coordinates one complete AEGIS application run.
    """

    def __init__(
        self,
        adapter: MarketAdapter,
        aegis: AEGIS,
    ) -> None:

        self._adapter = adapter
        self._aegis = aegis

    def run(
        self,
        instrument: Instrument,
        timeframe: Timeframe,
        candle_count: int,
    ) -> ProcessResult:

        candle_series = self._adapter.get_candles(
            instrument=instrument,
            timeframe=timeframe,
            count=candle_count,
        )

        return self._aegis.process(
            candle_series,
        )