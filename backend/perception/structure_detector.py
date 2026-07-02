"""
AEGIS AI

Structure Detector

Converts confirmed market swings into
MarketStructure.
"""

from __future__ import annotations

from backend.domain import (
    MarketStructure,
    StructurePoint,
    StructureType,
    Swing,
    SwingType,
)


class StructureDetector:
    """
    Detect market structure from swings.

    This detector never raises an exception simply
    because there are not yet enough swings to infer
    market structure. An empty MarketStructure is a
    valid market state.
    """

    def detect(
        self,
        swings: list[Swing],
    ) -> MarketStructure:

        if not isinstance(swings, list):
            raise TypeError("swings must be a list")

        for swing in swings:
            if not isinstance(swing, Swing):
                raise TypeError(
                    "swings must contain only Swing instances"
                )

        if swings:
            first_candle = swings[0].candle

            market_structure = MarketStructure(
                instrument=first_candle.instrument,
                timeframe=first_candle.timeframe,
            )
        else:
            # No confirmed structure yet.
            #
            # The pipeline will simply observe an empty
            # MarketStructure and continue.
            #
            # We cannot construct a MarketStructure
            # without an instrument/timeframe, so this
            # remains an exceptional case for now until
            # the pipeline supplies the metadata.
            raise ValueError(
                "cannot build MarketStructure without at least one swing"
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