"""
AEGIS AI

Paper Execution Engine.
"""

from __future__ import annotations

from backend.application.execution.execution_engine import (
    ExecutionEngine,
)
from backend.domain import (
    ExecutionResult,
    ExecutionRequest,
)


class PaperExecutionEngine(ExecutionEngine):
    """
    Simulates trade execution without
    communicating with a broker.
    """

    def execute(
        self,
        execution_request: ExecutionRequest,
    ) -> ExecutionResult:

        return ExecutionResult(
            success=True,
            message="Paper trade executed successfully.",
        )