"""
Tests for the ProcessResultPresenter.
"""

from decimal import Decimal

from backend.application.process_result_presenter import (
    ProcessResultPresenter,
)
from backend.domain import (
    Decision,
    ExecutionResult,
    ProcessResult,
    RiskAssessment,
)
from backend.domain.decision import DecisionAction
from backend.domain import (
    Instrument,
    MarketContext,
    Timeframe,
)

def make_context() -> MarketContext:
    return MarketContext(
        instrument=Instrument(
            code="XAUUSD",
            name="Gold Spot",
        ),
        timeframe=Timeframe.M5,
    )

def make_result() -> ProcessResult:
    return ProcessResult(
        decision=Decision(
            action=DecisionAction.BUY,
            confidence=Decimal("0.85"),
            evidence=[],
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


def test_present_returns_string() -> None:

    presenter = ProcessResultPresenter()

    output = presenter.present(
        make_context(),
        make_result(),
    )

    assert isinstance(
        output,
        str,
    )

    assert "XAUUSD" in output
    assert "M5" in output
    assert "BUY" in output
    assert "0.85" in output
    assert "Risk accepted." in output
    assert "Paper trade executed." in output