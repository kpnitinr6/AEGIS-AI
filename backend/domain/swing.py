"""
AEGIS AI Domain

Represents a confirmed market swing.
"""

from __future__ import annotations

from dataclasses import dataclass

from backend.domain.price import Price
from backend.domain.timeframe import Timeframe
from backend.domain.swing_type import SwingType


@dataclass(frozen=True, slots=True)
class Swing:
    """
    Immutable value object representing a confirmed market swing.
    """

    timeframe: Timeframe
    type: SwingType
    price: Price

    def __post_init__(self) -> None:
        if not isinstance(self.timeframe, Timeframe):
            raise TypeError("timeframe must be a Timeframe")

        if not isinstance(self.type, SwingType):
            raise TypeError("type must be a SwingType")

        if not isinstance(self.price, Price):
            raise TypeError("price must be a Price")