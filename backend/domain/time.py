"""
AEGIS AI Domain

Represents a point in time when a market fact occurred.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone


@dataclass(frozen=True, slots=True)
class Time:
    """
    Immutable point in time.

    A domain value object representing when a market fact occurred.
    """

    value: datetime

    def __post_init__(self) -> None:
        if not isinstance(self.value, datetime):
            raise TypeError("value must be a datetime instance")

        # AEGIS stores all times internally as UTC.
        if self.value.tzinfo is None:
            object.__setattr__(
                self,
                "value",
                self.value.replace(tzinfo=timezone.utc),
            )
        else:
            object.__setattr__(
                self,
                "value",
                self.value.astimezone(timezone.utc),
            )

    def before(self, other: "Time") -> bool:
        return self.value < other.value

    def after(self, other: "Time") -> bool:
        return self.value > other.value

    def duration_to(self, other: "Time") -> timedelta:
        return other.value - self.value

    def isoformat(self) -> str:
        return self.value.isoformat()

    def __str__(self) -> str:
        return self.isoformat()