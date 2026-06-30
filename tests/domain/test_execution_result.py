"""
Tests for the ExecutionResult domain model.
"""

from backend.domain.execution_result import ExecutionResult


def test_successful_execution() -> None:

    result = ExecutionResult(
        success=True,
        message="Trade executed successfully.",
    )

    assert result.success is True
    assert result.message == "Trade executed successfully."


def test_failed_execution() -> None:

    result = ExecutionResult(
        success=False,
        message="Execution rejected.",
    )

    assert result.success is False
    assert result.message == "Execution rejected."