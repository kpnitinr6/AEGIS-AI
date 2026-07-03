"""
AEGIS AI

Execution Request Factory.
"""

from __future__ import annotations

from backend.domain import (
    ExecutionRequest,
    TradeIntent,
)


class ExecutionRequestFactory:
    """
    Creates ExecutionRequest objects from
    approved TradeIntent objects.
    """

    def create(
        self,
        trade_intent: TradeIntent,
    ) -> ExecutionRequest:

        return ExecutionRequest(
            instrument=trade_intent.instrument,
            timeframe=trade_intent.timeframe,
            action=trade_intent.decision.action,
            confidence=trade_intent.decision.confidence,
        )