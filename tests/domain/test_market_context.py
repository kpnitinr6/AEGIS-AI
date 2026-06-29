"""
Tests for the MarketContext domain object.
"""

from datetime import datetime, timezone
from decimal import Decimal

import pytest

from backend.domain import (
    Candle,
    Instrument,
    MarketContext,
    Time,
    Timeframe,
)


def make_instrument() -> Instrument:

    return Instrument(
        code="XAUUSD",
        name="Gold Spot",
    )


def make_candle() -> Candle:

    return Candle(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        open_time=Time(
            datetime(
                2026,
                7,
                2,
                9,
                0,
                tzinfo=timezone.utc,
            )
        ),
        open=Decimal("3350"),
        high=Decimal("3360"),
        low=Decimal("3340"),
        close=Decimal("3355"),
        tick_volume=100,
    )


def test_create_valid_market_context() -> None:

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
    )

    assert context.instrument.code == "XAUUSD"
    assert context.timeframe == Timeframe.M5
    assert context.market_structure is None
    assert context.trend is None
    assert context.evidence == []
    assert context.liquidity_sweeps == []
    assert context.break_of_structures == []
    assert context.change_of_characters == []


def test_invalid_instrument() -> None:

    with pytest.raises(TypeError):
        MarketContext(
            instrument="XAUUSD",
            timeframe=Timeframe.M5,
        )


def test_invalid_timeframe() -> None:

    with pytest.raises(TypeError):
        MarketContext(
            instrument=make_instrument(),
            timeframe="M5",
        )


def test_invalid_evidence_list() -> None:

    with pytest.raises(TypeError):
        MarketContext(
            instrument=make_instrument(),
            timeframe=Timeframe.M5,
            evidence="invalid",
        )


def test_invalid_liquidity_sweeps_list() -> None:

    with pytest.raises(TypeError):
        MarketContext(
            instrument=make_instrument(),
            timeframe=Timeframe.M5,
            liquidity_sweeps="invalid",
        )


def test_invalid_break_of_structures_list() -> None:

    with pytest.raises(TypeError):
        MarketContext(
            instrument=make_instrument(),
            timeframe=Timeframe.M5,
            break_of_structures="invalid",
        )


def test_invalid_change_of_characters_list() -> None:

    with pytest.raises(TypeError):
        MarketContext(
            instrument=make_instrument(),
            timeframe=Timeframe.M5,
            change_of_characters="invalid",
        )


def test_invalid_evidence_item() -> None:

    with pytest.raises(TypeError):
        MarketContext(
            instrument=make_instrument(),
            timeframe=Timeframe.M5,
            evidence=["invalid"],
        )


def test_invalid_liquidity_sweep_item() -> None:

    with pytest.raises(TypeError):
        MarketContext(
            instrument=make_instrument(),
            timeframe=Timeframe.M5,
            liquidity_sweeps=["invalid"],
        )


def test_invalid_break_of_structure_item() -> None:

    with pytest.raises(TypeError):
        MarketContext(
            instrument=make_instrument(),
            timeframe=Timeframe.M5,
            break_of_structures=["invalid"],
        )


def test_invalid_change_of_character_item() -> None:

    with pytest.raises(TypeError):
        MarketContext(
            instrument=make_instrument(),
            timeframe=Timeframe.M5,
            change_of_characters=["invalid"],
        )