"""
Integration tests for the execution pipeline.
"""

from decimal import Decimal

from backend.application.execution.execution_coordinator import (
    ExecutionCoordinator,
)
from backend.application.execution.execution_queue import (
    ExecutionQueue,
)
from backend.application.execution.execution_queue_service import (
    ExecutionQueueService,
)
from backend.application.execution.execution_registry import (
    ExecutionRegistry,
)
from backend.application.execution.execution_request_factory import (
    ExecutionRequestFactory,
)
from backend.application.execution.paper_execution_engine import (
    PaperExecutionEngine,
)
from backend.domain import (
    Decision,
    DecisionAction,
    Evidence,
    EvidenceDirection,
    EvidenceSource,
    ExecutionRequest,
    ExecutionResult,
    Instrument,
    Timeframe,
    TradeIntent,
)


def make_coordinator() -> ExecutionCoordinator:

    registry = ExecutionRegistry()

    queue = ExecutionQueue()

    queue_service = ExecutionQueueService(
        queue,
    )

    return ExecutionCoordinator(
        registry=registry,
        queue_service=queue_service,
    )


def make_request() -> ExecutionRequest:

    decision = Decision(
        action=DecisionAction.BUY,
        confidence=Decimal("0.80"),
        evidence=[
            Evidence(
                source=EvidenceSource.STRUCTURE,
                direction=EvidenceDirection.BULLISH,
                reason="Bullish structure.",
            ),
        ],
    )

    trade_intent = TradeIntent(
        instrument=Instrument(
            code="XAUUSD",
            name="Gold",
        ),
        timeframe=Timeframe.M15,
        decision=decision,
    )

    factory = ExecutionRequestFactory()

    return factory.create(
        trade_intent,
    )


def test_execution_pipeline() -> None:
    """
    Verify the complete execution pipeline using
    the PaperExecutionEngine.
    """

    coordinator = make_coordinator()

    engine = PaperExecutionEngine()

    request = make_request()

    coordinator.submit(
        request,
    )

    pending = coordinator.next_request()

    assert pending == request

    result = engine.execute(
        pending,
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

    completed = coordinator.complete()

    assert completed == request

    assert coordinator.next_request() is None


def test_pipeline_preserves_request() -> None:
    """
    Ensure the request survives the full pipeline
    unchanged until completion.
    """

    coordinator = make_coordinator()

    request = make_request()

    coordinator.submit(
        request,
    )

    pending = coordinator.next_request()

    assert pending is not None

    assert pending.instrument.code == "XAUUSD"

    assert pending.timeframe == Timeframe.M15

    assert pending.action == DecisionAction.BUY

    assert pending.confidence == Decimal("0.80")