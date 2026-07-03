"""
AEGIS AI

Bridge communication layer.
"""

from .message_type import MessageType
from .protocol import BridgeProtocol

__all__ = [
    "MessageType",
    "BridgeProtocol",
]