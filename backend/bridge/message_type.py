"""
AEGIS AI

Bridge Message Types.
"""

from __future__ import annotations

from enum import Enum


class MessageType(str, Enum):
    """
    Every message exchanged between AEGIS
    and external execution agents.
    """

    STATUS = "STATUS"

    EXECUTION_REQUEST = (
        "EXECUTION_REQUEST"
    )

    EXECUTION_RESULT = (
        "EXECUTION_RESULT"
    )

    CANDLES_REQUEST = (
        "CANDLES_REQUEST"
    )

    CANDLES_RESPONSE = (
        "CANDLES_RESPONSE"
    )

    ACCOUNT_REQUEST = (
        "ACCOUNT_REQUEST"
    )

    ACCOUNT_RESPONSE = (
        "ACCOUNT_RESPONSE"
    )

    POSITIONS_REQUEST = (
        "POSITIONS_REQUEST"
    )

    POSITIONS_RESPONSE = (
        "POSITIONS_RESPONSE"
    )

    HEARTBEAT = (
        "HEARTBEAT"
    )