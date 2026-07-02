"""
AEGIS AI Domain

Represents the direction of an Order Block.
"""

from enum import Enum


class OrderBlockDirection(str, Enum):
    """
    Direction of a confirmed Order Block.
    """

    BULLISH = "BULLISH"
    BEARISH = "BEARISH"