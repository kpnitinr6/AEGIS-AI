"""
AEGIS AI Domain

Represents a confirmed Break Of Structure (BOS) event.
"""

from __future__ import annotations

from dataclasses import dataclass

from backend.domain.candle import Candle
from backend.domain.instrument import Instrument
from backend.domain.price import Price
from backend.domain.structure_point import StructurePoint
from backend.domain.timeframe import Timeframe


@dataclass(frozen=True, slots=True)
class BreakOfStructure:
    """
    Immutable domain event representing a confirmed Break Of Structure (BOS).

    A BOS occurs when price decisively breaks an existing structural level,
    confirming continuation of the prevailing market trend.

    This object records only confirmed market facts. It does not determine
    whether a BOS has occurred—that responsibility belongs to the perception
    layer.
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
            raise TypeError("break_price must be a Price")