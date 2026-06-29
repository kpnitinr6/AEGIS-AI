"""
AEGIS AI Domain

Represents the origin of a piece of market evidence.
"""

from enum import Enum


class EvidenceSource(str, Enum):
    """
    Identifies the domain that produced a piece of evidence.
    """

    STRUCTURE = "STRUCTURE"
    LIQUIDITY = "LIQUIDITY"
    ORDER_BLOCK = "ORDER_BLOCK"
    FAIR_VALUE_GAP = "FAIR_VALUE_GAP"
    DOW_THEORY = "DOW_THEORY"
    WYCKOFF = "WYCKOFF"
    VOLUME = "VOLUME"