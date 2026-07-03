"""
AEGIS AI

AEGIS Agent Bridge Server.
"""

from __future__ import annotations

import json
from decimal import Decimal
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer

from backend.adapters.serialization.execution_request_serializer import (
    ExecutionRequestSerializer,
)
from backend.application.execution.execution_coordinator import (
    ExecutionCoordinator,
)
from backend.application.execution.execution_queue import (
    ExecutionQueue,
)
from backend.application.execution.execution_queue_service import (
    ExecutionQueueService,
)
from backend.application.execution.execution_registry import (
    ExecutionRegistry,
)
from backend.domain import (
    DecisionAction,
    ExecutionRequest,
    Instrument,
    Timeframe,
)


SERIALIZER = ExecutionRequestSerializer()

REGISTRY = ExecutionRegistry()

QUEUE = ExecutionQueue()

QUEUE_SERVICE = ExecutionQueueService(
    QUEUE,
)

COORDINATOR = ExecutionCoordinator(
    registry=REGISTRY,
    queue_service=QUEUE_SERVICE,
)

# ------------------------------------------------------------------
# Temporary bootstrap request.
# This disappears once the Decision Engine starts producing
# ExecutionRequests.
# ------------------------------------------------------------------

COORDINATOR.submit(
    ExecutionRequest(
        instrument=Instrument(
            code="XAUUSD",
            name="Gold",
        ),
        timeframe=Timeframe.M15,
        action=DecisionAction.BUY,
        confidence=Decimal("0.80"),
    )
)


class BridgeHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/status":

            payload = {
                "status": "ok",
                "message": "Hello AEGIS Agent",
            }

        elif self.path == "/command":

            request = COORDINATOR.next_request()

            if request is None:

                payload = {
                    "action": "NONE",
                }

            else:

                payload = SERIALIZER.serialize(
                    request,
                )

        else:

            self.send_response(404)
            self.end_headers()
            return

        body = json.dumps(
            payload,
        ).encode("utf-8")

        self.send_response(200)

        self.send_header(
            "Content-Type",
            "application/json",
        )

        self.send_header(
            "Content-Length",
            str(len(body)),
        )

        self.end_headers()

        self.wfile.write(body)

    def log_message(
        self,
        format,
        *args,
    ):
        return


def main():

    server = HTTPServer(
        ("127.0.0.1", 8080),
        BridgeHandler,
    )

    print()
    print("=" * 60)
    print("AEGIS Agent Bridge")
    print("Listening on http://127.0.0.1:8080")
    print("=" * 60)
    print()

    server.serve_forever()


if __name__ == "__main__":
    main()