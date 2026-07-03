"""
Tests for ReplayEngine.
"""

from backend.application import (
    ApplicationRunResult,
)
from backend.application.factory import (
    create_aegis,
)
from backend.application.replay_engine import (
    ReplayEngine,
)
from backend.domain import (
    Instrument,
    Timeframe,
)
from backend.testing.scenarios.bullish_trend_scenario import (
    BullishTrendScenario,
)


def make_instrument() -> Instrument:
    return Instrument(
        code="XAUUSD",
        name="Gold Spot",
    )


def test_replay_returns_application_results() -> None:
    """
    Given a CandleSeries,
    when ReplayEngine replays it,
    then one ApplicationRunResult is produced
    for each candle in the series.
    """

    aegis = create_aegis()

    replay_engine = ReplayEngine(
        application=aegis,
    )

    scenario = BullishTrendScenario()

    candle_series = scenario.generate(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        count=20,
    )

    results = replay_engine.replay(
        candle_series,
    )

    assert len(results) == 19

    assert all(
        isinstance(
            result,
            ApplicationRunResult,
        )
        for result in results
    )