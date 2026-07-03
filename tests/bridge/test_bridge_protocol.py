"""
AEGIS AI

Tests for the BridgeProtocol.
"""

from __future__ import annotations

import pytest

from backend.bridge import (
    BridgeProtocol,
    MessageType,
)


def test_create_message() -> None:

    protocol = BridgeProtocol()

    message = protocol.create_message(
        MessageType.STATUS,
        {
            "status": "OK",
        },
    )

    assert message == {
        "type": "STATUS",
        "payload": {
            "status": "OK",
        },
    }


def test_validate_valid_message() -> None:

    protocol = BridgeProtocol()

    message = {
        "type": "STATUS",
        "payload": {
            "status": "OK",
        },
    }

    assert protocol.validate(message) is True


def test_validate_requires_type() -> None:

    protocol = BridgeProtocol()

    with pytest.raises(ValueError):

        protocol.validate(
            {
                "payload": {},
            }
        )


def test_validate_requires_payload() -> None:

    protocol = BridgeProtocol()

    with pytest.raises(ValueError):

        protocol.validate(
            {
                "type": "STATUS",
            }
        )


def test_validate_rejects_unknown_message_type() -> None:

    protocol = BridgeProtocol()

    with pytest.raises(ValueError):

        protocol.validate(
            {
                "type": "UNKNOWN",
                "payload": {},
            }
        )


def test_validate_requires_payload_dict() -> None:

    protocol = BridgeProtocol()

    with pytest.raises(TypeError):

        protocol.validate(
            {
                "type": "STATUS",
                "payload": "invalid",
            }
        )