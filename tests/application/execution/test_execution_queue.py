from decimal import Decimal

from backend.application.execution.execution_queue import (
    ExecutionQueue,
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


def test_queue_starts_empty():

    queue = ExecutionQueue()

    assert queue.is_empty()
    assert queue.size() == 0


def test_enqueue_increases_size():

    queue = ExecutionQueue()

    queue.enqueue(
        make_request(),
    )

    assert queue.size() == 1


def test_peek_does_not_remove():

    queue = ExecutionQueue()

    request = make_request()

    queue.enqueue(
        request,
    )

    assert queue.peek() == request
    assert queue.size() == 1


def test_dequeue_returns_request():

    queue = ExecutionQueue()

    request = make_request()

    queue.enqueue(
        request,
    )

    assert queue.dequeue() == request
    assert queue.is_empty()


def test_dequeue_empty_returns_none():

    queue = ExecutionQueue()

    assert queue.dequeue() is None