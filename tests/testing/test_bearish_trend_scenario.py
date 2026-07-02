"""
Tests for BearishTrendScenario.
"""

from backend.domain import (
    CandleSeries,
    Instrument,
    Timeframe,
)
from backend.testing.scenarios.bearish_trend_scenario import (
    BearishTrendScenario,
)


def test_generate_returns_candle_series() -> None:

    scenario = BearishTrendScenario()

    series = scenario.generate(
        instrument=Instrument(
            code="XAUUSD",
            name="Gold Spot",
        ),
        timeframe=Timeframe.M5,
        count=20,
    )

    assert isinstance(
        series,
        CandleSeries,
    )

    assert len(series) == 20

    assert (
        series.first().instrument.code
        == "XAUUSD"
    )

    assert (
        series.first().timeframe
        == Timeframe.M5
    )