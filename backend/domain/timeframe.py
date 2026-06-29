"""
AEGIS AI Domain

Supported market timeframes.
"""

from enum import Enum


class Timeframe(str, Enum):
    """
    Supported trading timeframes.

    Using an Enum prevents spelling mistakes and
    keeps the entire application consistent.
    """

    M1 = "M1"
    M5 = "M5"
    M15 = "M15"
    M30 = "M30"

    H1 = "H1"
    H4 = "H4"

    D1 = "D1"
    W1 = "W1"

    MN1 = "MN1"