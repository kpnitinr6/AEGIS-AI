"""
AEGIS AI Domain

Represents a structural event in the market.
"""

from enum import Enum


class StructureType(str, Enum):
    """
    Describes how a confirmed swing relates
    to previous market structure.
    """

    HIGHER_HIGH = "HH"
    HIGHER_LOW = "HL"
    LOWER_HIGH = "LH"
    LOWER_LOW = "LL"

    BREAK_OF_STRUCTURE = "BOS"

    CHANGE_OF_CHARACTER = "CHOCH"

    RANGE = "RANGE"