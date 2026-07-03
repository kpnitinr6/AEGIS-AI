"""
AEGIS AI

Execution Request Deserializer.
"""

from __future__ import annotations

from decimal import Decimal

from backend.domain import (
    DecisionAction,
    ExecutionRequest,
    Instrument,
    Timeframe,
)


class ExecutionRequestDeserializer:
    """
    Deserializes JSON-compatible dictionaries
    into ExecutionRequest objects.
    """

    def deserialize(
        self,
        payload: dict,
    ) -> ExecutionRequest:

        if not isinstance(
            payload,
            dict,
        ):
            raise TypeError(
                "payload must be a dict"
            )

        return ExecutionRequest(
            instrument=Instrument(
                code=str(
                    payload["instrument"],
                ),
                name=str(
                    payload["instrument"],
                ),
            ),
            timeframe=Timeframe(
                payload["timeframe"],
            ),
            action=DecisionAction[
                payload["action"]
            ],
            confidence=Decimal(
                payload["confidence"],
            ),
        )