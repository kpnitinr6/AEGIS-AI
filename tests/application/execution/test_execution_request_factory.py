"""
Tests for ExecutionRequestFactory.
"""

from decimal import Decimal

from backend.application.execution.execution_request_factory import (
    ExecutionRequestFactory,
)
from backend.domain import (
    Decision,
    DecisionAction,
    Evidence,
    EvidenceDirection,
    EvidenceSource,
    ExecutionRequest,
    Instrument,
    Timeframe,
    TradeIntent,
)


def make_trade_intent() -> TradeIntent:

    decision = Decision(
        action=DecisionAction.BUY,
        confidence=Decimal("0.80"),
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
            name="Gold",
        ),
        timeframe=Timeframe.M15,
        decision=decision,
    )


def test_factory_creates_execution_request() -> None:

    factory = ExecutionRequestFactory()

    request = factory.create(
        make_trade_intent(),
    )

    assert isinstance(
        request,
        ExecutionRequest,
    )

    assert request.instrument.code == "XAUUSD"

    assert request.timeframe == Timeframe.M15

    assert request.action == DecisionAction.BUY

    assert request.confidence == Decimal("0.80")


def test_factory_creates_new_request_instance() -> None:

    factory = ExecutionRequestFactory()

    first = factory.create(
        make_trade_intent(),
    )

    second = factory.create(
        make_trade_intent(),
    )

    assert first == second

    assert first is not second