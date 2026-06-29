"""
AEGIS AI Domain

Represents the direction of a liquidity sweep.
"""

from enum import Enum


class LiquiditySweepDirection(str, Enum):
    """
    Direction of a confirmed liquidity sweep.
    """

    BULLISH = "BULLISH"
    BEARISH = "BEARISH"