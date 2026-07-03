"""
Tests for HistoricalMarketAdapter.
"""

from pathlib import Path

from backend.adapters.historical.adapter import HistoricalMarketAdapter
from backend.domain import Instrument, Timeframe


def make_instrument() -> Instrument:
    return Instrument(
        code="XAUUSD",
        name="Gold Spot",
    )


def test_loads_historical_candles() -> None:

    adapter = HistoricalMarketAdapter(
        Path("datasets/sample/sample_gold_m5.csv")
    )

    series = adapter.get_candles(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        count=3,
    )

    assert len(series) == 3

    first = series.first()
    last = series.latest()

    assert first.instrument.code == "XAUUSD"
    assert first.timeframe == Timeframe.M5

    assert str(first.open) == "3300.00"
    assert str(first.close) == "3302.00"

    assert str(last.open) == "3304.00"
    assert str(last.close) == "3307.00"


def test_count_limits_returned_candles() -> None:

    adapter = HistoricalMarketAdapter(
        Path("datasets/sample/sample_gold_m5.csv")
    )

    series = adapter.get_candles(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        count=2,
    )

    assert len(series) == 2

    first = series.first()

    assert str(first.open) == "3302.00"
