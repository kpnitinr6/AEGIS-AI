"""
Tests for the FakeMarketAdapter.
"""

from decimal import Decimal

from backend.adapters.fake.adapter import FakeMarketAdapter
from backend.domain.instrument import Instrument
from backend.domain.time import Time
from backend.domain.timeframe import Timeframe


def make_instrument() -> Instrument:
    return Instrument(
        code="XAUUSD",
        name="Gold Spot",
    )


def test_returns_requested_number_of_candles() -> None:

    adapter = FakeMarketAdapter()

    candles = adapter.get_candles(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        count=10,
    )

    assert len(candles) == 10


def test_every_candle_uses_requested_instrument() -> None:

    instrument = make_instrument()

    adapter = FakeMarketAdapter()

    candles = adapter.get_candles(
        instrument=instrument,
        timeframe=Timeframe.M5,
        count=5,
    )

    for candle in candles:
        assert candle.instrument == instrument


def test_every_candle_has_correct_timeframe() -> None:

    adapter = FakeMarketAdapter()

    candles = adapter.get_candles(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        count=5,
    )

    for candle in candles:
        assert candle.timeframe == Timeframe.M5


def test_prices_are_decimals() -> None:

    adapter = FakeMarketAdapter()

    candles = adapter.get_candles(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        count=3,
    )

    for candle in candles:
        assert isinstance(candle.open, Decimal)
        assert isinstance(candle.high, Decimal)
        assert isinstance(candle.low, Decimal)
        assert isinstance(candle.close, Decimal)


def test_open_time_is_time_object() -> None:

    adapter = FakeMarketAdapter()

    candles = adapter.get_candles(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        count=2,
    )

    for candle in candles:
        assert isinstance(candle.open_time, Time)