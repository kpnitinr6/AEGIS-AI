"""
Tests for PerceptionPipeline.
"""

from datetime import datetime, timedelta, timezone
from decimal import Decimal

import pytest

from backend.domain import (
    Candle,
    CandleSeries,
    Instrument,
    MarketStructure,
    Time,
    Timeframe,
)
from backend.perception.pipeline import (
    PerceptionPipeline,
)


def make_instrument() -> Instrument:

    return Instrument(
        code="XAUUSD",
        name="Gold Spot",
    )


def make_candle(
    *,
    minute: int,
    high: str,
    low: str,
) -> Candle:

    return Candle(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        open_time=Time(
            datetime(
                2026,
                7,
                10,
                9,
                minute,
                tzinfo=timezone.utc,
            )
        ),
        open=Decimal(low),
        high=Decimal(high),
        low=Decimal(low),
        close=Decimal(high),
        tick_volume=100,
    )


def make_series_without_swings() -> CandleSeries:

    series = CandleSeries()

    series.add(
        make_candle(
            minute=0,
            high="10",
            low="5",
        )
    )

    series.add(
        make_candle(
            minute=5,
            high="11",
            low="6",
        )
    )

    return series


def make_series_with_swing() -> CandleSeries:

    series = CandleSeries()

    series.add(
        make_candle(
            minute=0,
            high="10",
            low="5",
        )
    )

    series.add(
        make_candle(
            minute=5,
            high="15",
            low="4",
        )
    )

    series.add(
        make_candle(
            minute=10,
            high="11",
            low="6",
        )
    )

    return series


def test_invalid_input() -> None:

    pipeline = PerceptionPipeline()

    with pytest.raises(TypeError):
        pipeline.detect("invalid")


def test_returns_empty_result_when_no_swings() -> None:

    pipeline = PerceptionPipeline()

    result = pipeline.detect(
        make_series_without_swings(),
    )

    assert result.swings == []

    assert result.market_structure is None


def test_detect_returns_market_structure() -> None:

    pipeline = PerceptionPipeline()

    result = pipeline.detect(
        make_series_with_swing(),
    )

    assert len(result.swings) == 1

    assert isinstance(
        result.market_structure,
        MarketStructure,
    )

    def test_detect_returns_break_of_structures_collection() -> None:
        pipeline = PerceptionPipeline()

        result = pipeline.detect(
            make_series_with_swing(),
        )

        assert isinstance(
            result.break_of_structures,
            list,
        )
def test_detect_returns_change_of_character_collection() -> None:

    pipeline = PerceptionPipeline()

    result = pipeline.detect(
        make_series_with_swing(),
    )

    assert isinstance(
        result.change_of_characters,
        list,
    )

def test_detect_returns_liquidity_sweep_collection() -> None:

    pipeline = PerceptionPipeline()

    result = pipeline.detect(
        make_series_with_swing(),
    )

    assert isinstance(
        result.liquidity_sweeps,
        list,
    )

def test_detect_returns_order_block_collection() -> None:

    pipeline = PerceptionPipeline()

    result = pipeline.detect(
        make_series_with_swing(),
    )

    assert isinstance(
        result.order_blocks,
        list,
    )
