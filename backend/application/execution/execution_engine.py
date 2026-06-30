"""
AEGIS AI

Execution Engine contract.
"""

from __future__ import annotations

from typing import Protocol

from backend.domain import (
    ExecutionResult,
    TradeIntent,
)


class ExecutionEngine(Protocol):
    """
    Contract implemented by every execution engine.
    """

    def execute(
        self,
        trade_intent: TradeIntent,
    ) -> ExecutionResult:
        """
        Execute a trade intent.
        """
        ...