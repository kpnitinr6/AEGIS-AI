"""
AEGIS AI Domain

Represents the directional implication of market evidence.
"""

from enum import Enum


class EvidenceDirection(str, Enum):
    """
    Direction supported by a piece of evidence.
    """

    BULLISH = "BULLISH"
    BEARISH = "BEARISH"
    NEUTRAL = "NEUTRAL"