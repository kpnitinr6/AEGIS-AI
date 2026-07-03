from __future__ import annotations

from decimal import Decimal

from backend.adapters.serialization import (
    ExecutionRequestSerializer,
)
from backend.domain import (
    DecisionAction,
    ExecutionRequest,
    Instrument,
    Timeframe,
)


def test_serialize_execution_request() -> None:

    serializer = ExecutionRequestSerializer()

    request = ExecutionRequest(
        instrument=Instrument(
            code="XAUUSD",
            name="Gold Spot",
        ),
        timeframe=Timeframe.M5,
        action=DecisionAction.BUY,
        confidence=Decimal("0.80"),
    )

    payload = serializer.serialize(
        request,
    )

    assert payload == {
        "instrument": "XAUUSD",
        "timeframe": "M5",
        "action": "BUY",
        "confidence": "0.80",
    }


def test_serialize_invalid_type() -> None:

    serializer = ExecutionRequestSerializer()

    try:
        serializer.serialize("invalid")
        assert False
    except TypeError:
        assert True