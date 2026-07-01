"""
AEGIS AI

Application facade.
"""

from __future__ import annotations

from backend.application.decision_engine import DecisionEngine
from backend.application.execution.paper_execution_engine import (
    PaperExecutionEngine,
)
from backend.application.risk_engine import RiskEngine
from backend.application.trade_intent_factory import (
    TradeIntentFactory,
)
from backend.domain import (
    MarketContext,
    ProcessResult,
)


class AEGIS:
    """
    Main application entry point.
    """

    def __init__(
        self,
        decision_engine: DecisionEngine,
        risk_engine: RiskEngine,
        execution_engine: PaperExecutionEngine,
        trade_intent_factory: TradeIntentFactory,
    ) -> None:

        self._decision_engine = decision_engine
        self._risk_engine = risk_engine
        self._execution_engine = execution_engine
        self._trade_intent_factory = (
            trade_intent_factory
        )

    def process(
        self,
        context: MarketContext,
    ) -> ProcessResult:

        decision = self._decision_engine.decide(
            context,
        )

        assessment = self._risk_engine.evaluate(
            decision,
        )

        execution_result = None

        trade_intent = (
            self._trade_intent_factory.create(
                context=context,
                decision=decision,
                assessment=assessment,
            )
        )

        if trade_intent is not None:
            execution_result = (
                self._execution_engine.execute(
                    trade_intent,
                )
            )

        return ProcessResult(
            decision=decision,
            risk_assessment=assessment,
            execution_result=execution_result,
        )