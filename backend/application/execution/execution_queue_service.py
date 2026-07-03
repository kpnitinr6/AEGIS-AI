"""
AEGIS AI

Execution Queue Service.
"""

from __future__ import annotations

from backend.application.execution.execution_queue import (
    ExecutionQueue,
)
from backend.domain import ExecutionRequest


class ExecutionQueueService:
    """
    Application service responsible for
    managing pending execution requests.
    """

    def __init__(
        self,
        queue: ExecutionQueue,
    ) -> None:

        self._queue = queue

    def submit(
        self,
        request: ExecutionRequest,
    ) -> None:

        self._queue.enqueue(
            request,
        )

    def next_request(
        self,
    ) -> ExecutionRequest | None:

        return self._queue.peek()

    def mark_completed(
        self,
    ) -> ExecutionRequest | None:

        return self._queue.dequeue()