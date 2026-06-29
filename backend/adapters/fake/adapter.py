"""
AEGIS AI

Fake Market Adapter

Used for development and testing.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from decimal import Decimal

from backend.adapters.base import MarketAdapter
from backend.domain.candle import Candle
from backend.domain.candle_series import CandleSeries
from backend.domain.instrument import Instrument
from backend.domain.time import Time
from backend.domain.timeframe import Timeframe


class FakeMarketAdapter(MarketAdapter):
    """
    Fake implementation of the MarketAdapter.

    Generates deterministic candles for testing.
    """

    def get_candles(
        self,
        instrument: Instrument,
        timeframe: Timeframe,
        count: int,
    ) -> CandleSeries:

        series = CandleSeries()

        now = datetime.now(timezone.utc)

        price = Decimal("3300.00")

        for index in range(count):

            candle = Candle(
                instrument=instrument,
                timeframe=timeframe,
                open_time=Time(
                    now - timedelta(minutes=count - index)
                ),
                open=price,
                high=price + Decimal("3.00"),
                low=price - Decimal("2.00"),
                close=price + Decimal("1.00"),
                tick_volume=1000 + index,
            )

            series.add(candle)

            price += Decimal("1.00")

        return series