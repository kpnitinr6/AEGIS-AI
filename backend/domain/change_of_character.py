"""
AEGIS AI Domain

Represents a confirmed Change Of Character (CHOCH) event.
"""

from __future__ import annotations

from dataclasses import dataclass

from backend.domain.candle import Candle
from backend.domain.instrument import Instrument
from backend.domain.price import Price
from backend.domain.structure_point import StructurePoint
from backend.domain.timeframe import Timeframe


@dataclass(frozen=True, slots=True)
class ChangeOfCharacter:
    """
    Immutable domain event representing a confirmed
    Change Of Character (CHOCH).

    A CHOCH occurs when price breaks the previous structural
    expectation, indicating a potential transition in market
    behaviour.

    This object records only confirmed market facts.
    Detection and interpretation belong to higher layers.
    """

    instrument: Instrument
    timeframe: Timeframe
    broken_structure: StructurePoint
    confirming_candle: Candle
    break_price: Price

    def __post_init__(self) -> None:

        if not isinstance(self.instrument, Instrument):
            raise TypeError("instrument must be an Instrument")

        if not isinstance(self.timeframe, Timeframe):
            raise TypeError("timeframe must be a Timeframe")

        if not isinstance(self.broken_structure, StructurePoint):
            raise TypeError(
                "broken_structure must be a StructurePoint"
            )

        if not isinstance(self.confirming_candle, Candle):
            raise TypeError(
                "confirming_candle must be a Candle"
            )

        if not isinstance(self.break_price, Price):
            raise TypeError(
                "break_price must be a Price"
            )