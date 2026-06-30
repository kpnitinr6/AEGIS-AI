"""
Tests for the PaperExecutionEngine.
"""

from backend.application.execution.paper_execution_engine import (
    PaperExecutionEngine,
)
from backend.domain import (
    ExecutionResult,
    TradeIntent,
    Decision,
    Evidence,
    EvidenceDirection,
    EvidenceSource,
    Instrument,
    Timeframe,
)
from backend.domain.decision import DecisionAction
from decimal import Decimal


def make_trade_intent() -> TradeIntent:

    decision = Decision(
        action=DecisionAction.BUY,
        confidence=Decimal("1.00"),
        evidence=[
            Evidence(
                source=EvidenceSource.STRUCTURE,
                direction=EvidenceDirection.BULLISH,
                reason="Bullish structure.",
            )
        ],
    )

    return TradeIntent(
        instrument=Instrument(
            code="XAUUSD",
            name="Gold Spot",
        ),
        timeframe=Timeframe.M5,
        decision=decision,
    )


def test_paper_execution_succeeds() -> None:

    engine = PaperExecutionEngine()

    result = engine.execute(
        make_trade_intent(),
    )

    assert isinstance(
        result,
        ExecutionResult,
    )

    assert result.success is True

    assert (
        result.message
        == "Paper trade executed successfully."
    )