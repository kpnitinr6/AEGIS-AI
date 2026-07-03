"""
AEGIS AI

Tests for RemoteExecutionEngine.
"""

from __future__ import annotations

from decimal import Decimal

from backend.application.execution.http_client import HttpClient
from backend.application.execution.remote_execution_engine import (
    RemoteExecutionEngine,
)
from backend.domain import (
    DecisionAction,
    ExecutionRequest,
    Instrument,
    Timeframe,
)


class FakeHttpClient(HttpClient):
    """
    Fake HTTP client used for testing.
    """

    def __init__(self) -> None:
        self.called = False
        self.url: str | None = None
        self.payload: dict[str, str] | None = None

    def post(
        self,
        url: str,
        payload: dict[str, str],
    ) -> dict:

        self.called = True
        self.url = url
        self.payload = payload

        return {
            "success": True,
            "message": "Remote paper trade executed.",
        }


def make_execution_request() -> ExecutionRequest:

    return ExecutionRequest(
        instrument=Instrument(
            code="XAUUSD",
            name="Gold Spot",
        ),
        timeframe=Timeframe.M5,
        action=DecisionAction.BUY,
        confidence=Decimal("0.80"),
    )


def test_remote_execution_engine_executes_request() -> None:

    http_client = FakeHttpClient()

    engine = RemoteExecutionEngine(
        endpoint="http://localhost:8000/execute",
        http_client=http_client,
    )

    result = engine.execute(
        make_execution_request(),
    )

    assert http_client.called is True

    assert (
        http_client.url
        == "http://localhost:8000/execute"
    )

    assert http_client.payload == {
        "instrument": "XAUUSD",
        "timeframe": "M5",
        "action": "BUY",
        "confidence": "0.80",
    }

    assert result.success is True
    assert (
        result.message
        == "Remote paper trade executed."
    )


def test_remote_execution_engine_requires_endpoint() -> None:

    try:

        RemoteExecutionEngine(
            endpoint="",
        )

        assert False

    except ValueError:

        assert True