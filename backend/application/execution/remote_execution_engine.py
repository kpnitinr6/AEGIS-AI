"""
AEGIS AI

Remote Execution Engine.
"""

from __future__ import annotations

from urllib.error import HTTPError, URLError

from backend.adapters.serialization import (
    ExecutionRequestSerializer,
    ExecutionResultSerializer,
)
from backend.application.execution.execution_engine import (
    ExecutionEngine,
)
from backend.application.execution.http_client import (
    HttpClient,
)
from backend.application.execution.urllib_http_client import (
    UrllibHttpClient,
)
from backend.domain import (
    ExecutionRequest,
    ExecutionResult,
)


class RemoteExecutionEngine(ExecutionEngine):
    """
    Executes trades using a remote execution service.
    """

    def __init__(
        self,
        endpoint: str,
        http_client: HttpClient | None = None,
        request_serializer: (
            ExecutionRequestSerializer | None
        ) = None,
        result_serializer: (
            ExecutionResultSerializer | None
        ) = None,
    ) -> None:

        if not endpoint.strip():
            raise ValueError(
                "endpoint cannot be empty"
            )

        self._endpoint = endpoint

        self._http_client = (
            http_client
            if http_client is not None
            else UrllibHttpClient()
        )

        self._request_serializer = (
            request_serializer
            if request_serializer is not None
            else ExecutionRequestSerializer()
        )

        self._result_serializer = (
            result_serializer
            if result_serializer is not None
            else ExecutionResultSerializer()
        )

    def execute(
        self,
        execution_request: ExecutionRequest,
    ) -> ExecutionResult:

        payload = self._request_serializer.serialize(
            execution_request,
        )

        try:

            response = self._http_client.post(
                self._endpoint,
                payload,
            )

            return self._result_serializer.deserialize(
                response,
            )

        except HTTPError as error:

            return ExecutionResult(
                success=False,
                message=f"HTTP error: {error.code}",
            )

        except URLError as error:

            return ExecutionResult(
                success=False,
                message=(
                    f"Connection failed: "
                    f"{error.reason}"
                ),
            )

        except Exception as error:

            return ExecutionResult(
                success=False,
                message=str(error),
            )