"""
AEGIS AI

Process Result Presenter.
"""

from __future__ import annotations

from backend.domain import ProcessResult


class ProcessResultPresenter:
    """
    Converts a ProcessResult into human-readable text.
    """

    def present(
        self,
        result: ProcessResult,
    ) -> str:

        execution = (
            result.execution_result.message
            if result.execution_result is not None
            else "Not executed."
        )

        return (
            f"Decision: {result.decision.action.name}\n"
            f"Confidence: {result.decision.confidence}\n"
            f"Risk: {result.risk_assessment.reason}\n"
            f"Execution: {execution}"
        )