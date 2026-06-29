"""
AEGIS AI Domain

Represents the confirmed market structure for an instrument and timeframe.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from backend.domain.instrument import Instrument
from backend.domain.structure_point import StructurePoint
from backend.domain.timeframe import Timeframe


@dataclass(slots=True)
class MarketStructure:
    """
    Aggregate root representing the confirmed market structure.

    A MarketStructure owns an ordered collection of StructurePoint objects.
    It represents market facts only and does not derive trend, bias,
    liquidity, or trading decisions.
    """

    instrument: Instrument
    timeframe: Timeframe
    structure_points: list[StructurePoint] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not isinstance(self.instrument, Instrument):
            raise TypeError("instrument must be an Instrument")

        if not isinstance(self.timeframe, Timeframe):
            raise TypeError("timeframe must be a Timeframe")

        if not isinstance(self.structure_points, list):
            raise TypeError("structure_points must be a list")

        for point in self.structure_points:
            if not isinstance(point, StructurePoint):
                raise TypeError(
                    "structure_points must contain only StructurePoint instances"
                )

    def append(self, point: StructurePoint) -> None:
        """Append a new StructurePoint."""

        if not isinstance(point, StructurePoint):
            raise TypeError("point must be a StructurePoint")

        self.structure_points.append(point)

    def latest(self) -> StructurePoint | None:
        """Return the most recent StructurePoint."""

        if not self.structure_points:
            return None

        return self.structure_points[-1]

    def previous(self) -> StructurePoint | None:
        """Return the previous StructurePoint."""

        if len(self.structure_points) < 2:
            return None

        return self.structure_points[-2]

    def __len__(self) -> int:
        return len(self.structure_points)