"""
AEGIS AI

Structure Detector

Converts confirmed market swings into
MarketStructure.
"""

from __future__ import annotations

from backend.domain import (
    Instrument,
    MarketStructure,
    StructurePoint,
    StructureType,
    Swing,
    SwingType,
    Timeframe,
)


class StructureDetector:
    """
    Detect market structure from swings.
    """

    def detect(
        self,
        swings: list[Swing],
    ) -> MarketStructure:

        if not isinstance(swings, list):
            raise TypeError("swings must be a list")

        if not swings:
            raise ValueError("swings cannot be empty")

        for swing in swings:
            if not isinstance(swing, Swing):
                raise TypeError(
                    "swings must contain only Swing instances"
                )

        first_candle = swings[0].candle

        market_structure = MarketStructure(
            instrument=first_candle.instrument,
            timeframe=first_candle.timeframe,
        )

        previous_high: Swing | None = None
        previous_low: Swing | None = None

        for swing in swings:

            if swing.type == SwingType.HIGH:

                if previous_high is None:
                    structure = StructureType.HIGHER_HIGH

                elif (
                    swing.candle.high
                    > previous_high.candle.high
                ):
                    structure = StructureType.HIGHER_HIGH

                else:
                    structure = StructureType.LOWER_HIGH

                previous_high = swing

            else:

                if previous_low is None:
                    structure = StructureType.LOWER_LOW

                elif (
                    swing.candle.low
                    > previous_low.candle.low
                ):
                    structure = StructureType.HIGHER_LOW

                else:
                    structure = StructureType.LOWER_LOW

                previous_low = swing

            market_structure.append(
                StructurePoint(
                    structure=structure,
                    swing=swing,
                )
            )

        return market_structure