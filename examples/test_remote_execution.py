"""
AEGIS AI

End-to-end test of the RemoteExecutionEngine.

Requires AEGIS-Relay to be running on localhost:8000.
"""

from __future__ import annotations

from decimal import Decimal

from backend.application.execution.remote_execution_engine import (
    RemoteExecutionEngine,
)
from backend.domain import (
    DecisionAction,
    ExecutionRequest,
    Instrument,
    Timeframe,
)


def main() -> None:

    engine = RemoteExecutionEngine(
        endpoint="http://127.0.0.1:8000/execute",
    )

    request = ExecutionRequest(
        instrument=Instrument(
            code="XAUUSD",
            name="Gold Spot",
        ),
        timeframe=Timeframe.M5,
        action=DecisionAction.BUY,
        confidence=Decimal("0.80"),
    )

    result = engine.execute(
        request,
    )

    print()
    print("=" * 60)
    print("AEGIS REMOTE EXECUTION TEST")
    print("=" * 60)

    print(f"Success : {result.success}")
    print(f"Message : {result.message}")

    print("=" * 60)
    print()


if __name__ == "__main__":
    main()