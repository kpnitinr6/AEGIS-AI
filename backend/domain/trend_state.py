"""
AEGIS AI Domain

Represents the directional state of the market.
"""

from enum import Enum


class TrendState(str, Enum):
    """
    The current directional state of market structure.
    """

    BULLISH = "BULLISH"
    BEARISH = "BEARISH"
    SIDEWAYS = "SIDEWAYS"
    UNKNOWN = "UNKNOWN"