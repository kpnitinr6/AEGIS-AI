"""
Tests for the ProcessResult domain model.
"""

from decimal import Decimal

from backend.domain import (
    Decision,
    ExecutionResult,
    ProcessResult,
    RiskAssessment,
)
from backend.domain.decision import DecisionAction


def test_process_result() -> None:

    result = ProcessResult(
        decision=Decision(
            action=DecisionAction.BUY,
            confidence=Decimal("0.95"),
            evidence=[],
        ),
        risk_assessment=RiskAssessment(
            approved=True,
            reason="Risk accepted.",
        ),
        execution_result=ExecutionResult(
            success=True,
            message="Paper trade executed successfully.",
        ),
    )

    assert result.decision.action == DecisionAction.BUY

    assert result.risk_assessment.approved is True

    assert result.execution_result is not None

    assert result.execution_result.success is True


def test_process_result_without_execution() -> None:

    result = ProcessResult(
        decision=Decision(
            action=DecisionAction.NO_TRADE,
            confidence=Decimal("0.00"),
            evidence=[],
        ),
        risk_assessment=RiskAssessment(
            approved=False,
            reason="No trade.",
        ),
        execution_result=None,
    )

    assert result.execution_result is None