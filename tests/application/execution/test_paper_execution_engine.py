"""
Tests for PaperExecutionEngine.
"""

from decimal import Decimal

from backend.application.execution.paper_execution_engine import (
    PaperExecutionEngine,
)
from backend.domain import (
    DecisionAction,
    ExecutionRequest,
    Instrument,
    Timeframe,
)


def make_request() -> ExecutionRequest:

    return ExecutionRequest(
        instrument=Instrument(
            code="XAUUSD",
            name="Gold",
        ),
        timeframe=Timeframe.M15,
        action=DecisionAction.BUY,
        confidence=Decimal("0.80"),
    )


def test_execute_returns_success():

    engine = PaperExecutionEngine()

    result = engine.execute(
        make_request(),
    )

    assert result.success is True

    assert result.message == (
        "Paper trade executed successfully."
    )


def test_execute_returns_execution_result():

    engine = PaperExecutionEngine()

    result = engine.execute(
        make_request(),
    )

    assert result.success