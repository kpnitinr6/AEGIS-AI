"""
AEGIS AI

Command Dispatcher.
"""

from __future__ import annotations

from backend.bridge import (
    BridgeProtocol,
    MessageType,
)


class CommandDispatcher:
    """
    Dispatches bridge messages received
    from the AEGIS Bridge Server.
    """

    def __init__(
        self,
    ) -> None:

        self._protocol = BridgeProtocol()

    def dispatch(
        self,
        message: dict,
    ) -> MessageType:

        self._protocol.validate(
            message,
        )

        return MessageType(
            message["type"],
        )