"""
Tests for ReplayPresenter.
"""

from datetime import datetime, timezone
from decimal import Decimal

from backend.application.application_run_result import (
    ApplicationRunResult,
)
from backend.application.replay_presenter import (
    ReplayPresenter,
)
from backend.domain import (
    Candle,
    Decision,
    Evidence,
    EvidenceDirection,
    EvidenceSource,
    ExecutionResult,
    Instrument,
    MarketContext,
    MarketStructure,
    ProcessResult,
    RiskAssessment,
    StructurePoint,
    StructureType,
    Swing,
    SwingType,
    Time,
    Timeframe,
    Trend,
    TrendState,
)
from backend.domain.decision import (
    DecisionAction,
)


def make_instrument() -> Instrument:
    return Instrument(
        code="XAUUSD",
        name="Gold Spot",
    )


def make_candle() -> Candle:

    instrument = make_instrument()

    return Candle(
        instrument=instrument,
        timeframe=Timeframe.M5,
        open_time=Time(
            datetime(
                2026,
                7,
                1,
                9,
                0,
                tzinfo=timezone.utc,
            )
        ),
        open=Decimal("3300"),
        high=Decimal("3310"),
        low=Decimal("3290"),
        close=Decimal("3305"),
        tick_volume=100,
    )


def make_run_result() -> ApplicationRunResult:

    candle = make_candle()

    structure = MarketStructure(
        instrument=candle.instrument,
        timeframe=candle.timeframe,
    )

    structure.append(
        StructurePoint(
            structure=StructureType.HIGHER_HIGH,
            swing=Swing(
                candle=candle,
                type=SwingType.HIGH,
            ),
        )
    )

    context = MarketContext(
        instrument=candle.instrument,
        timeframe=candle.timeframe,
        market_structure=structure,
        trend=Trend(
            state=TrendState.BULLISH,
            market_structure=structure,
        ),
    )

    process = ProcessResult(
        decision=Decision(
            action=DecisionAction.BUY,
            confidence=Decimal("0.80"),
            evidence=[
                Evidence(
                    source=EvidenceSource.TREND,
                    direction=EvidenceDirection.BULLISH,
                    reason="Bullish trend.",
                )
            ],
        ),
        risk_assessment=RiskAssessment(
            approved=True,
            reason="Risk accepted.",
        ),
        execution_result=ExecutionResult(
            success=True,
            message="Paper trade executed.",
        ),
    )

    return ApplicationRunResult(
        context=context,
        result=process,
    )


def test_present_returns_string() -> None:

    presenter = ReplayPresenter()

    output = presenter.present(
        make_run_result(),
    )

    assert isinstance(
        output,
        str,
    )

    assert "XAUUSD" in output
    assert "M5" in output
    assert "BULLISH" in output
    assert "HIGHER_HIGH" in output
    assert "BUY" in output
    assert "0.80" in output
    assert "Bullish trend." in output
    assert "Risk accepted." in output
    assert "Paper trade executed." in output