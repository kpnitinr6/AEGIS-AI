"""
Behavior tests for the AEGIS application.

These tests exercise the complete production
application using realistic market scenarios.
"""

from backend.application import (
    ApplicationRunResult,
)
from backend.application.factory import (
    create_aegis,
)
from backend.domain import (
    Instrument,
    ProcessResult,
    Timeframe,
)
from backend.testing.scenarios.bearish_trend_scenario import (
    BearishTrendScenario,
)
from backend.testing.scenarios.bullish_trend_scenario import (
    BullishTrendScenario,
)
from backend.testing.scenarios.range_scenario import (
    RangeScenario,
)


def make_instrument() -> Instrument:
    return Instrument(
        code="XAUUSD",
        name="Gold Spot",
    )


def test_aegis_processes_bullish_trend_scenario() -> None:
    """
    Given a bullish market scenario,
    when AEGIS processes the candles,
    then a complete application result is produced.
    """

    aegis = create_aegis()

    scenario = BullishTrendScenario()

    candle_series = scenario.generate(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        count=20,
    )

    run_result = aegis.process(
        candle_series,
    )

    assert isinstance(
        run_result,
        ApplicationRunResult,
    )

    assert (
        run_result.context.instrument.code
        == "XAUUSD"
    )

    assert (
        run_result.context.timeframe
        == Timeframe.M5
    )

    assert isinstance(
        run_result.result,
        ProcessResult,
    )

    assert run_result.result.decision is not None

    assert (
        run_result.result.risk_assessment
        is not None
    )


def test_aegis_processes_bearish_trend_scenario() -> None:
    """
    Given a bearish market scenario,
    when AEGIS processes the candles,
    then a complete application result is produced.
    """

    aegis = create_aegis()

    scenario = BearishTrendScenario()

    candle_series = scenario.generate(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        count=20,
    )

    run_result = aegis.process(
        candle_series,
    )

    assert isinstance(
        run_result,
        ApplicationRunResult,
    )

    assert (
        run_result.context.instrument.code
        == "XAUUSD"
    )

    assert (
        run_result.context.timeframe
        == Timeframe.M5
    )

    assert isinstance(
        run_result.result,
        ProcessResult,
    )

    assert run_result.result.decision is not None

    assert (
        run_result.result.risk_assessment
        is not None
    )


def test_aegis_processes_range_scenario() -> None:
    """
    Given a ranging market scenario,
    when AEGIS processes the candles,
    then a complete application result is produced.
    """

    aegis = create_aegis()

    scenario = RangeScenario()

    candle_series = scenario.generate(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        count=20,
    )

    run_result = aegis.process(
        candle_series,
    )

    assert isinstance(
        run_result,
        ApplicationRunResult,
    )

    assert (
        run_result.context.instrument.code
        == "XAUUSD"
    )

    assert (
        run_result.context.timeframe
        == Timeframe.M5
    )

    assert isinstance(
        run_result.result,
        ProcessResult,
    )

    assert run_result.result.decision is not None

    assert (
        run_result.result.risk_assessment
        is not None
    )