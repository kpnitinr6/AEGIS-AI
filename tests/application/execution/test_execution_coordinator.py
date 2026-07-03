"""
Tests for ExecutionCoordinator.
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
from backend.domain import (
    DecisionAction,
    ExecutionRequest,
    Instrument,
    Timeframe,
)


def make_request() -> ExecutionRequest:

    return ExecutionRequest(
        instrument=Instrument(
            code="XAUUSD",
            name="Gold",
        ),
        timeframe=Timeframe.M15,
        action=DecisionAction.BUY,
        confidence=Decimal("0.80"),
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


def test_submit_registers_request():

    registry = ExecutionRegistry()

    queue = ExecutionQueue()

    queue_service = ExecutionQueueService(
        queue,
    )

    coordinator = ExecutionCoordinator(
        registry=registry,
        queue_service=queue_service,
    )

    request = make_request()

    coordinator.submit(
        request,
    )

    assert registry.size() == 1
    assert queue.size() == 1


def test_next_request_returns_request():

    coordinator = make_coordinator()

    request = make_request()

    coordinator.submit(
        request,
    )

    assert coordinator.next_request() == request


def test_complete_removes_request_from_queue():

    coordinator = make_coordinator()

    request = make_request()

    coordinator.submit(
        request,
    )

    completed = coordinator.complete()

    assert completed == request
    assert coordinator.next_request() is None


def test_next_request_empty_returns_none():

    coordinator = make_coordinator()

    assert coordinator.next_request() is None