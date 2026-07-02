"""
AEGIS AI

Liquidity Sweep Detector.

Detects confirmed liquidity sweeps from confirmed
market swings and subsequent price action.
"""

from __future__ import annotations

from backend.domain import (
    CandleSeries,
    LiquiditySweep,
    LiquiditySweepDirection,
    Swing,
    SwingType,
)


class LiquiditySweepDetector:
    """
    Detect confirmed liquidity sweeps.

    Version 1

    Bullish Sweep

        Swing Low
            ↓
        Candle low trades below swing low
            ↓
        Candle closes back above swing low

    Bearish Sweep

        Swing High
            ↓
        Candle high trades above swing high
            ↓
        Candle closes back below swing high
    """

    def detect(
        self,
        swings: list[Swing],
        candle_series: CandleSeries,
    ) -> list[LiquiditySweep]:

        if not isinstance(swings, list):
            raise TypeError("swings must be a list")

        if not isinstance(candle_series, CandleSeries):
            raise TypeError(
                "candle_series must be a CandleSeries"
            )

        for swing in swings:
            if not isinstance(swing, Swing):
                raise TypeError(
                    "swings must contain only Swing instances"
                )

        sweeps: list[LiquiditySweep] = []

        for swing in swings:

            future_candles = candle_series.candles_after(
                swing.candle,
            )

            if swing.type == SwingType.LOW:

                level = swing.candle.low

                for candle in future_candles:

                    if (
                        candle.low < level
                        and candle.close > level
                    ):
                        sweeps.append(
                            LiquiditySweep(
                                direction=LiquiditySweepDirection.BULLISH,
                                swept_swing=swing,
                                sweep_candle=candle,
                            )
                        )
                        break

            else:

                level = swing.candle.high

                for candle in future_candles:

                    if (
                        candle.high > level
                        and candle.close < level
                    ):
                        sweeps.append(
                            LiquiditySweep(
                                direction=LiquiditySweepDirection.BEARISH,
                                swept_swing=swing,
                                sweep_candle=candle,
                            )
                        )
                        break

        return sweeps