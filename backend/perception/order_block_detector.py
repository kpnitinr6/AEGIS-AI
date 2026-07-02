"""
AEGIS AI

Order Block Detector.

Detects confirmed Order Blocks from a confirmed
Break Of Structure.
"""

from __future__ import annotations

from backend.domain import (
    BreakOfStructure,
    CandleSeries,
    OrderBlock,
    OrderBlockDirection,
)


class OrderBlockDetector:
    """
    Detect confirmed Order Blocks.

    Version 1

    Bullish

        Last bearish candle immediately before
        a bullish BOS confirmation candle.

    Bearish

        Last bullish candle immediately before
        a bearish BOS confirmation candle.
    """

    def detect(
        self,
        candle_series: CandleSeries,
        bos: BreakOfStructure,
    ) -> OrderBlock | None:

        if not isinstance(
            candle_series,
            CandleSeries,
        ):
            raise TypeError(
                "candle_series must be a CandleSeries"
            )

        if not isinstance(
            bos,
            BreakOfStructure,
        ):
            raise TypeError(
                "bos must be a BreakOfStructure"
            )

        origin = candle_series.previous_of(
            bos.confirming_candle,
        )

        if origin is None:
            return None

        bullish = (
            bos.confirming_candle.close
            > bos.confirming_candle.open
        )

        bearish = (
            bos.confirming_candle.close
            < bos.confirming_candle.open
        )

        if bullish:

            if origin.close >= origin.open:
                return None

            return OrderBlock(
                instrument=bos.instrument,
                timeframe=bos.timeframe,
                direction=OrderBlockDirection.BULLISH,
                origin_candle=origin,
            )

        if bearish:

            if origin.close <= origin.open:
                return None

            return OrderBlock(
                instrument=bos.instrument,
                timeframe=bos.timeframe,
                direction=OrderBlockDirection.BEARISH,
                origin_candle=origin,
            )

        return None