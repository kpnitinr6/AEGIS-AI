"""
Tests for ExecutionQueueService.
"""

from decimal import Decimal

from backend.application.execution.execution_queue import (
    ExecutionQueue,
)
from backend.application.execution.execution_queue_service import (
    ExecutionQueueService,
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


def test_submit_adds_request_to_queue():

    queue = ExecutionQueue()

    service = ExecutionQueueService(
        queue,
    )

    request = make_request()

    service.submit(
        request,
    )

    assert queue.size() == 1


def test_next_request_returns_first_request():

    queue = ExecutionQueue()

    service = ExecutionQueueService(
        queue,
    )

    request = make_request()

    service.submit(
        request,
    )

    assert service.next_request() == request


def test_mark_completed_removes_request():

    queue = ExecutionQueue()

    service = ExecutionQueueService(
        queue,
    )

    request = make_request()

    service.submit(
        request,
    )

    completed = service.mark_completed()

    assert completed == request
    assert queue.is_empty()


def test_next_request_returns_none_when_queue_empty():

    queue = ExecutionQueue()

    service = ExecutionQueueService(
        queue,
    )

    assert service.next_request() is None


def test_mark_completed_returns_none_when_queue_empty():

    queue = ExecutionQueue()

    service = ExecutionQueueService(
        queue,
    )

    assert service.mark_completed() is None