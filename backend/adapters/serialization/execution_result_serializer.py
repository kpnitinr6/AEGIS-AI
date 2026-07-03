"""
AEGIS AI

Execution Result Serializer.
"""

from __future__ import annotations

from backend.domain import ExecutionResult


class ExecutionResultSerializer:
    """
    Deserializes execution results received
    from a remote execution service.
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