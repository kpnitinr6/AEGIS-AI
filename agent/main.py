"""
AEGIS AI

MT5 Agent.
"""

from __future__ import annotations

import time

from agent.command_dispatcher import (
    CommandDispatcher,
)
from agent.http_client import (
    AgentHttpClient,
)


def main() -> None:
    """
    Main MT5 Agent loop.
    """

    client = AgentHttpClient(
        "http://127.0.0.1:8080",
    )

    dispatcher = CommandDispatcher()

    print()
    print("=" * 60)
    print("AEGIS MT5 Agent")
    print("Waiting for commands...")
    print("=" * 60)
    print()

    while True:

        try:

            message = client.get(
                "/command",
            )

            message_type = dispatcher.dispatch(
                message,
            )

            print(
                f"Received: {message_type.value}"
            )

        except Exception as error:

            print(
                f"Agent error: {error}"
            )

        time.sleep(
            1,
        )


if __name__ == "__main__":
    main()