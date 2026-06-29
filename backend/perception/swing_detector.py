"""
AEGIS AI

Swing Detector

The SwingDetector is the first component of the Perception Layer.

It observes a CandleSeries and identifies confirmed swing highs
and swing lows using a simple three-candle pattern.

This detector makes no trading decisions.
It only converts market facts into domain objects.
"""

from __future__ import annotations

from backend.domain import (
    CandleSeries,
    Swing,
    SwingType,
)


class SwingDetector:
    """
    Detect confirmed market swings.

    Version 1:

    Swing High:
        previous.high < current.high > next.high

    Swing Low:
        previous.low > current.low < next.low
    """

    def detect(
        self,
        candles: CandleSeries,
    ) -> list[Swing]:
        """
        Detect confirmed swings.

        Parameters
        ----------
        candles:
            Completed candle series.

        Returns
        -------
        list[Swing]
            Swings ordered chronologically.
        """

        if not isinstance(candles, CandleSeries):
            raise TypeError("candles must be a CandleSeries")

        if len(candles) < 3:
            return []

        candle_list = list(candles)

        swings: list[Swing] = []

        for index in range(1, len(candle_list) - 1):

            previous = candle_list[index - 1]
            current = candle_list[index]
            following = candle_list[index + 1]

            if (
                current.high > previous.high
                and current.high > following.high
            ):
                swings.append(
                    Swing(
                        candle=current,
                        type=SwingType.HIGH,
                    )
                )

            elif (
                current.low < previous.low
                and current.low < following.low
            ):
                swings.append(
                    Swing(
                        candle=current,
                        type=SwingType.LOW,
                    )
                )

        return swings