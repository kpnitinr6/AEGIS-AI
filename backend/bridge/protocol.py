"""
AEGIS AI

Bridge Protocol.
"""

from __future__ import annotations

from backend.bridge.message_type import (
    MessageType,
)


class BridgeProtocol:
    """
    Creates and validates bridge messages exchanged
    between AEGIS and external execution agents.
    """

    def create_message(
        self,
        message_type: MessageType,
        payload: dict,
    ) -> dict:

        if not isinstance(
            message_type,
            MessageType,
        ):
            raise TypeError(
                "message_type must be a MessageType"
            )

        if not isinstance(
            payload,
            dict,
        ):
            raise TypeError(
                "payload must be a dict"
            )

        return {
            "type": message_type.value,
            "payload": payload,
        }

    def validate(
        self,
        message: dict,
    ) -> bool:
        """
        Validate a bridge message.

        Returns True if the message conforms to the
        protocol. Raises an exception otherwise.
        """

        if not isinstance(
            message,
            dict,
        ):
            raise TypeError(
                "message must be a dict"
            )

        if "type" not in message:
            raise ValueError(
                "message missing 'type'"
            )

        if "payload" not in message:
            raise ValueError(
                "message missing 'payload'"
            )

        try:

            MessageType(
                message["type"],
            )

        except ValueError as error:

            raise ValueError(
                "unknown message type"
            ) from error

        if not isinstance(
            message["payload"],
            dict,
        ):
            raise TypeError(
                "payload must be a dict"
            )

        return True