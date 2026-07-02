"""
Tests for the ProcessResultPresenter.
"""

from decimal import Decimal

from backend.application.process_result_presenter import (
    ProcessResultPresenter,
)
from backend.domain import (
    Decision,
    Evidence,
    EvidenceDirection,
    EvidenceSource,
    ExecutionResult,
    Instrument,
    MarketContext,
    ProcessResult,
    RiskAssessment,
    Timeframe,
)
from backend.domain.decision import (
    DecisionAction,
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
            evidence=[
                Evidence(
                    source=EvidenceSource.LIQUIDITY_SWEEP,
                    direction=EvidenceDirection.BULLISH,
                    reason="Confirmed bullish liquidity sweep.",
                ),
                Evidence(
                    source=EvidenceSource.BREAK_OF_STRUCTURE,
                    direction=EvidenceDirection.BULLISH,
                    reason="Confirmed bullish Break Of Structure.",
                ),
                Evidence(
                    source=EvidenceSource.TREND,
                    direction=EvidenceDirection.BULLISH,
                    reason="Bullish market trend.",
                ),
                Evidence(
                    source=EvidenceSource.STRUCTURE,
                    direction=EvidenceDirection.BULLISH,
                    reason="Latest confirmed structure is a Higher High.",
                ),
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


def test_present_returns_string() -> None:

    presenter = ProcessResultPresenter()

    output = presenter.present(
        make_context(),
        make_result(),
    )

    assert isinstance(output, str)

    assert "XAUUSD" in output
    assert "M5" in output
    assert "BUY" in output
    assert "0.85" in output
    assert "Risk accepted." in output
    assert "Paper trade executed." in output


def test_evidence_is_presented_in_priority_order() -> None:

    presenter = ProcessResultPresenter()

    output = presenter.present(
        make_context(),
        make_result(),
    )

    trend = output.index(
        "Bullish market trend."
    )

    structure = output.index(
        "Latest confirmed structure is a Higher High."
    )

    bos = output.index(
        "Confirmed bullish Break Of Structure."
    )

    liquidity = output.index(
        "Confirmed bullish liquidity sweep."
    )

    assert trend < structure < bos < liquidity


def test_present_handles_empty_evidence() -> None:

    presenter = ProcessResultPresenter()

    result = ProcessResult(
        decision=Decision(
            action=DecisionAction.HOLD,
            confidence=Decimal("0.00"),
            evidence=[],
        ),
        risk_assessment=RiskAssessment(
            approved=False,
            reason="No trade.",
        ),
        execution_result=None,
    )

    output = presenter.present(
        make_context(),
        result,
    )

    assert "No supporting evidence." in output