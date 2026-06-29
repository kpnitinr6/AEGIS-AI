"""
AEGIS AI Domain

Represents the observed price of an instrument at a specific point in time.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from backend.domain.instrument import Instrument
from backend.domain.time import Time


@dataclass(frozen=True, slots=True)
class Price:
    """
    Immutable value object representing a market price.
    """

    instrument: Instrument
    amount: Decimal
    time: Time

    def __post_init__(self) -> None:
        if not isinstance(self.instrument, Instrument):
            raise TypeError("instrument must be an Instrument")

        if not isinstance(self.amount, Decimal):
            raise TypeError("amount must be a Decimal")

        if not isinstance(self.time, Time):
            raise TypeError("time must be a Time")