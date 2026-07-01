"""
Tests for the AEGIS application runner.
"""

from backend.adapters.fake import FakeMarketAdapter
from backend.application import (
    ApplicationRunResult,
)
from backend.application.aegis import AEGIS
from backend.application.application_service import (
    ApplicationService,
)
from backend.application.decision_engine import DecisionEngine
from backend.application.execution.paper_execution_engine import (
    PaperExecutionEngine,
)
from backend.application.market_analyzer import MarketAnalyzer
from backend.application.process_result_presenter import (
    ProcessResultPresenter,
)
from backend.application.risk_engine import RiskEngine
from backend.application.trade_intent_factory import (
    TradeIntentFactory,
)
from backend.domain import (
    Instrument,
    Timeframe,
)
from backend.domain.policies.majority_vote_policy import (
    MajorityVotePolicy,
)


def test_runner_can_present_process_result() -> None:

    application = ApplicationService(
        adapter=FakeMarketAdapter(),
        aegis=AEGIS(
            market_analyzer=MarketAnalyzer(),
            decision_engine=DecisionEngine(
                reasoners=[],
                policy=MajorityVotePolicy(),
            ),
            risk_engine=RiskEngine(),
            execution_engine=PaperExecutionEngine(),
            trade_intent_factory=TradeIntentFactory(),
        ),
    )

    presenter = ProcessResultPresenter()

    run_result = application.run(
        instrument=Instrument(
            code="XAUUSD",
            name="Gold Spot",
        ),
        timeframe=Timeframe.M5,
        candle_count=200,
    )

    assert isinstance(
        run_result,
        ApplicationRunResult,
    )

    output = presenter.present(
        run_result.context,
        run_result.result,
    )

    assert isinstance(output, str)
    assert len(output) > 0
    assert "XAUUSD" in output
    assert "M5" in output