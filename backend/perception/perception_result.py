"""
AEGIS AI

Perception Result.

Represents the output of the perception layer.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from backend.domain import (
    BreakOfStructure,
    MarketStructure,
    Swing,
)


@dataclass(frozen=True, slots=True)
class PerceptionResult:
    """
    Immutable result produced by the PerceptionPipeline.
    """

    swings: list[Swing] = field(default_factory=list)

    market_structure: MarketStructure | None = None

    break_of_structures: list[
        BreakOfStructure
    ] = field(default_factory=list)