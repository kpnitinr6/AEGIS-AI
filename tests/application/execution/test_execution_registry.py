"""
Tests for ExecutionRegistry.
"""

from decimal import Decimal

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


def test_registry_starts_empty():

    registry = ExecutionRegistry()

    assert registry.size() == 0
    assert registry.all() == ()


def test_register_adds_request():

    registry = ExecutionRegistry()

    request = make_request()

    registry.register(
        request,
    )

    assert registry.size() == 1
    assert registry.all() == (
        request,
    )


def test_clear_removes_all_requests():

    registry = ExecutionRegistry()

    registry.register(
        make_request(),
    )

    registry.clear()

    assert registry.size() == 0
    assert registry.all() == ()


def test_register_requires_execution_request():

    registry = ExecutionRegistry()

    try:

        registry.register(
            "invalid",  # type: ignore[arg-type]
        )

        assert False

    except TypeError:

        pass