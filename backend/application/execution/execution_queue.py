"""
AEGIS AI

Execution Queue.
"""

from __future__ import annotations

from collections import deque

from backend.domain import ExecutionRequest


class ExecutionQueue:
    """
    In-memory FIFO queue for ExecutionRequest objects.

    The queue represents pending execution work waiting
    to be collected by an execution agent.
    """

    def __init__(self) -> None:

        self._queue: deque[ExecutionRequest] = deque()

    def enqueue(
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

        self._queue.append(
            request,
        )

    def dequeue(
        self,
    ) -> ExecutionRequest | None:

        if not self._queue:
            return None

        return self._queue.popleft()

    def peek(
        self,
    ) -> ExecutionRequest | None:

        if not self._queue:
            return None

        return self._queue[0]

    def is_empty(
        self,
    ) -> bool:

        return len(
            self._queue
        ) == 0

    def size(
        self,
    ) -> int:

        return len(
            self._queue
        )