"""
AEGIS AI

Execution Engine contract.
"""

from __future__ import annotations

from typing import Protocol

from backend.domain import (
    ExecutionRequest,
    ExecutionResult,
)


class ExecutionEngine(Protocol):
    """
    Contract implemented by every execution engine.
    """

    def execute(
        self,
        execution_request: ExecutionRequest,
    ) -> ExecutionResult:
        """
        Execute an execution request.
        """
        ...