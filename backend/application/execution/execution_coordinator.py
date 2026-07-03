"""
AEGIS AI

Execution Coordinator.
"""

from __future__ import annotations

from backend.application.execution.execution_queue_service import (
    ExecutionQueueService,
)
from backend.application.execution.execution_registry import (
    ExecutionRegistry,
)
from backend.domain import ExecutionRequest


class ExecutionCoordinator:
    """
    Coordinates the submission of execution
    requests throughout the execution subsystem.

    The coordinator is the single entry point
    for scheduling execution requests.
    """

    def __init__(
        self,
        registry: ExecutionRegistry,
        queue_service: ExecutionQueueService,
    ) -> None:

        self._registry = registry
        self._queue_service = queue_service

    def submit(
        self,
        request: ExecutionRequest,
    ) -> None:
        """
        Register the request and make it
        available for execution.
        """

        self._registry.register(
            request,
        )

        self._queue_service.submit(
            request,
        )

    def next_request(
        self,
    ) -> ExecutionRequest | None:
        """
        Return the next pending execution request.
        """

        return self._queue_service.next_request()

    def complete(
        self,
    ) -> ExecutionRequest | None:
        """
        Mark the oldest queued request as completed.
        """

        return self._queue_service.mark_completed()