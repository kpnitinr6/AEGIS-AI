"""
AEGIS AI Domain

Represents a market swing.
"""

from __future__ import annotations

from dataclasses import dataclass

from backend.domain.candle import Candle
from backend.domain.swing_type import SwingType


@dataclass(frozen=True, slots=True)
class Swing:
    """
    Immutable market swing.

    A swing identifies a candle that represents
    a significant turning point.
    """

    candle: Candle
    type: SwingType

    def __post_init__(self) -> None:

        if not isinstance(self.candle, Candle):
            raise TypeError("candle must be a Candle")

        if not isinstance(self.type, SwingType):
            raise TypeError("type must be a SwingType")