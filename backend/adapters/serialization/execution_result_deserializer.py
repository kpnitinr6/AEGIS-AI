"""
AEGIS AI

Execution Result Deserializer.
"""

from __future__ import annotations

from backend.domain import ExecutionResult


class ExecutionResultDeserializer:
    """
    Deserializes JSON-compatible dictionaries
    into ExecutionResult objects.
    """

    def deserialize(
        self,
        payload: dict,
    ) -> ExecutionResult:

        if not isinstance(
            payload,
            dict,
        ):
            raise TypeError(
                "payload must be a dict"
            )

        return ExecutionResult(
            success=bool(
                payload["success"],
            ),
            message=str(
                payload["message"],
            ),
        )