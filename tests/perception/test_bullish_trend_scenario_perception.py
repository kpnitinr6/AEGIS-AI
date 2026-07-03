"""
Tests that the BullishTrendScenario produces
market perception.

The purpose of these tests is not to verify
trading decisions. Instead, they verify that
the synthetic market data is rich enough for
the perception layer to begin understanding
market structure.
"""

from backend.domain import (
    Instrument,
    Timeframe,
)
from backend.perception.pipeline import (
    PerceptionPipeline,
)
from backend.testing.scenarios.bullish_trend_scenario import (
    BullishTrendScenario,
)


def make_instrument() -> Instrument:
    return Instrument(
        code="XAUUSD",
        name="Gold Spot",
    )


def test_bullish_scenario_produces_swings() -> None:
    """
    A realistic bullish trend should produce
    confirmed swing points.
    """

    scenario = BullishTrendScenario()

    candle_series = scenario.generate(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        count=20,
    )

    perception = PerceptionPipeline().detect(
        candle_series,
    )

    assert len(
        perception.swings
    ) > 0


def test_bullish_scenario_produces_market_structure() -> None:
    """
    Once swings exist, the perception layer
    should be capable of producing a
    MarketStructure.
    """

    scenario = BullishTrendScenario()

    candle_series = scenario.generate(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        count=20,
    )

    perception = PerceptionPipeline().detect(
        candle_series,
    )

    assert (
        perception.market_structure
        is not None
    )


def test_market_structure_contains_points() -> None:
    """
    The generated MarketStructure should contain
    at least one StructurePoint.
    """

    scenario = BullishTrendScenario()

    candle_series = scenario.generate(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        count=20,
    )

    perception = PerceptionPipeline().detect(
        candle_series,
    )

    assert (
        perception.market_structure
        is not None
    )

    assert (
        len(
            perception.market_structure
        )
        > 0
    )