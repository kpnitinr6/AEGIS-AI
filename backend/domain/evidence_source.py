"""
AEGIS AI Domain

Represents the origin of a piece of market evidence.
"""

from enum import Enum


class EvidenceSource(str, Enum):
    """
    Identifies the market event or analytical method
    that produced a piece of evidence.
    """

    BREAK_OF_STRUCTURE = "BREAK_OF_STRUCTURE"

    CHANGE_OF_CHARACTER = "CHANGE_OF_CHARACTER"

    MARKET_SHIFT = "MARKET_SHIFT"

    LIQUIDITY_SWEEP = "LIQUIDITY_SWEEP"

    ORDER_BLOCK = "ORDER_BLOCK"

    FAIR_VALUE_GAP = "FAIR_VALUE_GAP"

    TREND = "TREND"

    STRUCTURE = "STRUCTURE"

    DOW_THEORY = "DOW_THEORY"

    WYCKOFF = "WYCKOFF"

    VOLUME = "VOLUME"

