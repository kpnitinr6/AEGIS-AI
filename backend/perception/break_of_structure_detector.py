"""
AEGIS AI

Break Of Structure Detector.

Detects confirmed Break Of Structure (BOS) events
from an existing MarketStructure.
"""

from __future__ import annotations

from backend.domain import (
    BreakOfStructure,
    MarketStructure,
    Price,
    StructureType,
)


class BreakOfStructureDetector:
    """
    Detect confirmed Break Of Structure events.

    Version 1

    Bullish BOS:
        Higher High -> Higher Low

    Bearish BOS:
        Lower High -> Lower Low
    """

    def detect(
        self,
        market_structure: MarketStructure,
    ) -> BreakOfStructure | None:

        if not isinstance(
            market_structure,
            MarketStructure,
        ):
            raise TypeError(
                "market_structure must be a MarketStructure"
            )

        if len(market_structure) < 2:
            return None

        previous = market_structure.previous()
        latest = market_structure.latest()

        assert previous is not None
        assert latest is not None

        bullish = (
            previous.structure
            == StructureType.HIGHER_HIGH
            and latest.structure
            == StructureType.HIGHER_LOW
        )

        bearish = (
            previous.structure
            == StructureType.LOWER_HIGH
            and latest.structure
            == StructureType.LOWER_LOW
        )

        if not (bullish or bearish):
            return None

        candle = latest.swing.candle

        return BreakOfStructure(
            instrument=market_structure.instrument,
            timeframe=market_structure.timeframe,
            broken_structure=previous,
            confirming_candle=candle,
            break_price=Price(
                instrument=candle.instrument,
                amount=candle.close,
                time=candle.open_time,
            ),
        )