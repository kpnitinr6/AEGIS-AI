"""
AEGIS AI

Fake Market Adapter

Used for development and testing.
"""

from datetime import datetime, timedelta

from backend.adapters.base import MarketAdapter
from backend.domain.candle import Candle
from backend.domain.candle_series import CandleSeries
from backend.domain.timeframe import Timeframe


class FakeMarketAdapter(MarketAdapter):
    """
    Generates fake candles.

    Used for testing architecture before
    connecting to MT5.
    """

    def get_candles(
        self,
        symbol: str,
        timeframe: Timeframe,
        count: int,
    ) -> CandleSeries:

        series = CandleSeries()

        now = datetime.now()

        price = 3300.0

        for i in range(count):

            candle = Candle(
                symbol=symbol,
                timeframe=timeframe,
                timestamp=now - timedelta(minutes=count - i),

                open=price,
                high=price + 3,
                low=price - 2,
                close=price + 1,

                tick_volume=1000 + i,
            )

            series.add(candle)

            price += 1

        return series