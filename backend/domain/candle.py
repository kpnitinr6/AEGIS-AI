"""
AEGIS AI Domain

Immutable market candle.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from backend.domain.instrument import Instrument
from backend.domain.time import Time
from backend.domain.timeframe import Timeframe


@dataclass(frozen=True, slots=True)
class Candle:
    """
    Represents one completed market candle.

    This object contains only factual market data.
    """

    instrument: Instrument
    timeframe: Timeframe

    open_time: Time

    open: Decimal
    high: Decimal
    low: Decimal
    close: Decimal

    tick_volume: int

    real_volume: int | None = None
    spread: int | None = None

    def __post_init__(self) -> None:
        if not isinstance(self.instrument, Instrument):
            raise TypeError("instrument must be an Instrument")

        if not isinstance(self.timeframe, Timeframe):
            raise TypeError("timeframe must be a Timeframe")

        if not isinstance(self.open_time, Time):
            raise TypeError("open_time must be a Time")

        for field_name in ("open", "high", "low", "close"):
            if not isinstance(getattr(self, field_name), Decimal):
                raise TypeError(f"{field_name} must be a Decimal")

        if not isinstance(self.tick_volume, int):
            raise TypeError("tick_volume must be an int")

        if self.real_volume is not None and not isinstance(self.real_volume, int):
            raise TypeError("real_volume must be an int or None")

        if self.spread is not None and not isinstance(self.spread, int):
            raise TypeError("spread must be an int or None")