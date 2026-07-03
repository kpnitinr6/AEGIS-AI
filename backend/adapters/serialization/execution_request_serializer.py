"""
AEGIS AI

Execution Request Serializer.
"""

from __future__ import annotations

from backend.domain import ExecutionRequest


class ExecutionRequestSerializer:
    """
    Serializes ExecutionRequest objects into
    JSON-compatible dictionaries.
    """

    def serialize(
        self,
        request: ExecutionRequest,
    ) -> dict[str, str]:

        if not isinstance(
            request,
            ExecutionRequest,
        ):
            raise TypeError(
                "request must be an ExecutionRequest"
            )

        return {
            "instrument": request.instrument.code,
            "timeframe": request.timeframe.value,
            "action": request.action.name,
            "confidence": str(
                request.confidence,
            ),
        }