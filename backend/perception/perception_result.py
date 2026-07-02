"""
AEGIS AI

Perception Result.

Represents the complete output of the perception layer.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from backend.domain import (
    BreakOfStructure,
    ChangeOfCharacter,
    LiquiditySweep,
    MarketStructure,
    OrderBlock,
    Swing,
)


@dataclass(frozen=True, slots=True)
class PerceptionResult:
    """
    Immutable result produced by the PerceptionPipeline.
    """

    swings: list[Swing] = field(
        default_factory=list
    )

    market_structure: MarketStructure | None = None

    break_of_structures: list[
        BreakOfStructure
    ] = field(default_factory=list)

    change_of_characters: list[
        ChangeOfCharacter
    ] = field(default_factory=list)

    liquidity_sweeps: list[
        LiquiditySweep
    ] = field(default_factory=list)

    order_blocks: list[
        OrderBlock
    ] = field(default_factory=list)