"""
AEGIS AI Domain

Represents a confirmed liquidity sweep.
"""

from __future__ import annotations

from dataclasses import dataclass

from backend.domain.candle import Candle
from backend.domain.liquidity_sweep_direction import (
    LiquiditySweepDirection,
)
from backend.domain.swing import Swing


@dataclass(frozen=True, slots=True)
class LiquiditySweep:
    """
    Immutable value object representing a confirmed
    liquidity sweep.

    A liquidity sweep occurs when price temporarily
    trades beyond a confirmed swing before rejecting
    back into the prior range.
    """

    direction: LiquiditySweepDirection
    swept_swing: Swing
    sweep_candle: Candle

    def __post_init__(self) -> None:

        if not isinstance(
            self.direction,
            LiquiditySweepDirection,
        ):
            raise TypeError(
                "direction must be a LiquiditySweepDirection"
            )

        if not isinstance(
            self.swept_swing,
            Swing,
        ):
            raise TypeError(
                "swept_swing must be a Swing"
            )

        if not isinstance(
            self.sweep_candle,
            Candle,
        ):
            raise TypeError(
                "sweep_candle must be a Candle"
            )