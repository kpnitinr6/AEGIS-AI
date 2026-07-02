"""
AEGIS AI

Change Of Character Detector.

Detects confirmed Change Of Character (CHOCH) events
from an existing MarketStructure.
"""

from __future__ import annotations

from backend.domain import (
    ChangeOfCharacter,
    MarketStructure,
    Price,
    StructureType,
)


class ChangeOfCharacterDetector:
    """
    Detect confirmed Change Of Character events.

    Version 1

    Bullish CHOCH:
        Lower Low -> Higher High

    Bearish CHOCH:
        Higher High -> Lower Low
    """

    def detect(
        self,
        market_structure: MarketStructure,
    ) -> ChangeOfCharacter | None:

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
            previous.structure == StructureType.LOWER_LOW
            and latest.structure == StructureType.HIGHER_HIGH
        )

        bearish = (
            previous.structure == StructureType.HIGHER_HIGH
            and latest.structure == StructureType.LOWER_LOW
        )

        if not (bullish or bearish):
            return None

        candle = latest.swing.candle

        return ChangeOfCharacter(
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