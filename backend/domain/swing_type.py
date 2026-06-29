"""
AEGIS AI Domain

Represents the type of a market swing.
"""

from enum import Enum


class SwingType(str, Enum):
    """
    The direction of a confirmed market swing.
    """

    HIGH = "HIGH"
    LOW = "LOW"