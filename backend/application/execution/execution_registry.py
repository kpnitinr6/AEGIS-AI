"""
AEGIS AI

Execution Registry.
"""

from __future__ import annotations

from backend.domain import ExecutionRequest


class ExecutionRegistry:
    """
    Stores ExecutionRequest objects that have
    been submitted by the Brain.

    This registry allows the Brain to inspect
    pending execution work independently from
    the execution queue.
    """

    def __init__(self) -> None:

        self._requests: list[
            ExecutionRequest
        ] = []

    def register(
        self,
        request: ExecutionRequest,
    ) -> None:

        if not isinstance(
            request,
            ExecutionRequest,
        ):
            raise TypeError(
                "request must be an ExecutionRequest"
            )

        self._requests.append(
            request,
        )

    def all(
        self,
    ) -> tuple[
        ExecutionRequest,
        ...
    ]:

        return tuple(
            self._requests,
        )

    def size(
        self,
    ) -> int:

        return len(
            self._requests,
        )

    def clear(
        self,
    ) -> None:

        self._requests.clear()