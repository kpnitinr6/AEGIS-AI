"""
Tests for the AEGIS application facade.
"""

from backend.application.aegis import AEGIS
from backend.application.decision_engine import DecisionEngine
from backend.application.execution.paper_execution_engine import (
    PaperExecutionEngine,
)
from backend.application.risk_engine import RiskEngine
from backend.application.trade_intent_factory import (
    TradeIntentFactory,
)
from backend.domain import (
    Instrument,
    MarketContext,
    ProcessResult,
    Timeframe,
)
from backend.domain.policies.majority_vote_policy import (
    MajorityVotePolicy,
)


def make_context() -> MarketContext:

    instrument = Instrument(
        code="XAUUSD",
        name="Gold Spot",
    )

    return MarketContext(
        instrument=instrument,
        timeframe=Timeframe.M5,
    )


def test_process_returns_process_result() -> None:

    aegis = AEGIS(
        decision_engine=DecisionEngine(
            reasoners=[],
            policy=MajorityVotePolicy(),
        ),
        risk_engine=RiskEngine(),
        execution_engine=PaperExecutionEngine(),
        trade_intent_factory=TradeIntentFactory(),
    )

    result = aegis.process(
        make_context(),
    )

    assert isinstance(
        result,
        ProcessResult,
    )

    assert result.decision.action.name == "NO_TRADE"
    assert result.risk_assessment.approved is False
    assert result.execution_result is None