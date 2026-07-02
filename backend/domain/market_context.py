"""
AEGIS AI Domain

Represents the current market context.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from backend.domain.break_of_structure import BreakOfStructure
from backend.domain.change_of_character import ChangeOfCharacter
from backend.domain.evidence import Evidence
from backend.domain.instrument import Instrument
from backend.domain.liquidity_sweep import LiquiditySweep
from backend.domain.market_structure import MarketStructure
from backend.domain.timeframe import Timeframe
from backend.domain.order_block import (
    OrderBlock,
)
from backend.domain.trend import Trend


@dataclass(slots=True)
class MarketContext:
    """
    Aggregate root representing AEGIS' current understanding
    of the market for a single instrument and timeframe.

    Unlike value objects, MarketContext evolves as new
    confirmed market events are observed.

    It contains references to market facts but performs
    no reasoning or trading decisions.
    """

    instrument: Instrument
    timeframe: Timeframe

    market_structure: MarketStructure | None = None
    trend: Trend | None = None

    evidence: list[Evidence] = field(default_factory=list)

    liquidity_sweeps: list[LiquiditySweep] = field(
        default_factory=list
    )
    order_blocks: list[OrderBlock] = field(
        default_factory=list,
    )
    break_of_structures: list[
        BreakOfStructure
    ] = field(default_factory=list)

    change_of_characters: list[
        ChangeOfCharacter
    ] = field(default_factory=list)

    def __post_init__(self) -> None:

        if not isinstance(self.instrument, Instrument):
            raise TypeError(
                "instrument must be an Instrument"
            )

        if not isinstance(self.timeframe, Timeframe):
            raise TypeError(
                "timeframe must be a Timeframe"
            )

        if self.market_structure is not None and not isinstance(
            self.market_structure,
            MarketStructure,
        ):
            raise TypeError(
                "market_structure must be a MarketStructure or None"
            )

        if self.trend is not None and not isinstance(
            self.trend,
            Trend,
        ):
            raise TypeError(
                "trend must be a Trend or None"
            )

        for item in self.evidence:
            if not isinstance(item, Evidence):
                raise TypeError(
                    "evidence must contain only Evidence instances"
                )

        for item in self.liquidity_sweeps:
            if not isinstance(item, LiquiditySweep):
                raise TypeError(
                    "liquidity_sweeps must contain only LiquiditySweep instances"
                )

        for item in self.order_blocks:
            if not isinstance(
                    item,
                    OrderBlock,
            ):
                raise TypeError(
                    "order_blocks must contain only OrderBlock instances"
                )

        for item in self.break_of_structures:
            if not isinstance(item, BreakOfStructure):
                raise TypeError(
                    "break_of_structures must contain only BreakOfStructure instances"
                )

        for item in self.change_of_characters:
            if not isinstance(item, ChangeOfCharacter):
                raise TypeError(
                    "change_of_characters must contain only ChangeOfCharacter instances"
                )