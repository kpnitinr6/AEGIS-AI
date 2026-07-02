"""
AEGIS AI Domain

Represents a confirmed Order Block.
"""

from __future__ import annotations

from dataclasses import dataclass

from backend.domain.candle import Candle
from backend.domain.instrument import Instrument
from backend.domain.order_block_direction import (
    OrderBlockDirection,
)
from backend.domain.timeframe import Timeframe


@dataclass(frozen=True, slots=True)
class OrderBlock:
    """
    Immutable domain event representing a confirmed
    Order Block.

    Version 1

    A bullish Order Block is the final bearish candle
    before a confirmed bullish Break Of Structure.

    A bearish Order Block is the final bullish candle
    before a confirmed bearish Break Of Structure.

    This object records only the confirmed market fact.
    Detection belongs to the perception layer.
    """

    instrument: Instrument
    timeframe: Timeframe
    direction: OrderBlockDirection
    origin_candle: Candle

    def __post_init__(self) -> None:

        if not isinstance(
            self.instrument,
            Instrument,
        ):
            raise TypeError(
                "instrument must be an Instrument"
            )

        if not isinstance(
            self.timeframe,
            Timeframe,
        ):
            raise TypeError(
                "timeframe must be a Timeframe"
            )

        if not isinstance(
            self.direction,
            OrderBlockDirection,
        ):
            raise TypeError(
                "direction must be an OrderBlockDirection"
            )

        if not isinstance(
            self.origin_candle,
            Candle,
        ):
            raise TypeError(
                "origin_candle must be a Candle"
            )