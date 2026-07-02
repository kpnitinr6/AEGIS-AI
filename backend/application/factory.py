"""
AEGIS AI

Application Factory.

Builds the default AEGIS application using the
standard production configuration.
"""

from __future__ import annotations

from backend.application.aegis import AEGIS
from backend.application.decision_engine import DecisionEngine
from backend.application.execution.paper_execution_engine import (
    PaperExecutionEngine,
)
from backend.application.market_analyzer import (
    MarketAnalyzer,
)
from backend.application.risk_engine import RiskEngine
from backend.application.trade_intent_factory import (
    TradeIntentFactory,
)
from backend.domain.policies.majority_vote_policy import (
    MajorityVotePolicy,
)
from backend.reasoning import (
    BOSReasoner,
    CHOCHReasoner,
    LiquiditySweepReasoner,
    StructureReasoner,
    TrendReasoner,
)


def create_aegis() -> AEGIS:
    """
    Create a fully configured AEGIS application using
    the default production components.
    """

    return AEGIS(
        market_analyzer=MarketAnalyzer(),
        decision_engine=DecisionEngine(
            reasoners=[
                TrendReasoner(),
                StructureReasoner(),
                BOSReasoner(),
                CHOCHReasoner(),
                LiquiditySweepReasoner(),
            ],
            policy=MajorityVotePolicy(),
        ),
        risk_engine=RiskEngine(),
        execution_engine=PaperExecutionEngine(),
        trade_intent_factory=TradeIntentFactory(),
    )