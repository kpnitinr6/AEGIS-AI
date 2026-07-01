"""
Tests for the AEGIS application facade.
"""

from datetime import datetime, timezone
from decimal import Decimal

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
from backend.domain import (
    Candle,
    CandleSeries,
    Instrument,
    ProcessResult,
    Time,
    Timeframe,
)
from backend.domain.policies.majority_vote_policy import (
    MajorityVotePolicy,
)


def make_instrument() -> Instrument:
    return Instrument(
        code="XAUUSD",
        name="Gold Spot",
    )


def make_candle_series() -> CandleSeries:

    instrument = make_instrument()

    series = CandleSeries()

    series.add(
        Candle(
            instrument=instrument,
            timeframe=Timeframe.M5,
            open_time=Time(
                datetime(
                    2026,
                    7,
                    1,
                    9,
                    0,
                    tzinfo=timezone.utc,
                )
            ),
            open=Decimal("3300"),
            high=Decimal("3310"),
            low=Decimal("3290"),
            close=Decimal("3305"),
            tick_volume=100,
        )
    )

    series.add(
        Candle(
            instrument=instrument,
            timeframe=Timeframe.M5,
            open_time=Time(
                datetime(
                    2026,
                    7,
                    1,
                    9,
                    5,
                    tzinfo=timezone.utc,
                )
            ),
            open=Decimal("3305"),
            high=Decimal("3312"),
            low=Decimal("3301"),
            close=Decimal("3308"),
            tick_volume=120,
        )
    )

    return series


def test_process_returns_process_result() -> None:

    aegis = AEGIS(
        market_analyzer=MarketAnalyzer(),
        decision_engine=DecisionEngine(
            reasoners=[],
            policy=MajorityVotePolicy(),
        ),
        risk_engine=RiskEngine(),
        execution_engine=PaperExecutionEngine(),
        trade_intent_factory=TradeIntentFactory(),
    )

    result = aegis.process(
        make_candle_series(),
    )

    assert isinstance(
        result,
        ProcessResult,
    )

    assert result.decision.action.name == "NO_TRADE"
    assert result.risk_assessment.approved is False
    assert result.execution_result is None