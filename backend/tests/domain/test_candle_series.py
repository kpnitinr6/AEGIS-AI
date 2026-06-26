from datetime import datetime

from backend.domain.candle import Candle
from backend.domain.candle_series import CandleSeries
from backend.domain.timeframe import Timeframe


def test_add_candle():

    series = CandleSeries()

    candle = Candle(
        symbol="XAUUSD",
        timeframe=Timeframe.M15,
        timestamp=datetime.now(),
        open=3300,
        high=3310,
        low=3295,
        close=3308,
        tick_volume=1200,
    )

    series.add(candle)

    assert len(series) == 1
    assert series.latest() == candle