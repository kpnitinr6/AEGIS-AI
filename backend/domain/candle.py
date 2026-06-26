"""
AEGIS AI Domain

Immutable market candle.
"""

from dataclasses import dataclass
from datetime import datetime

from backend.domain.timeframe import Timeframe


@dataclass(frozen=True, slots=True)
class Candle:
    """
    Represents one completed market candle.

    This object contains only factual market data.
    """

    symbol: str
    timeframe: Timeframe

    timestamp: datetime

    open: float
    high: float
    low: float
    close: float

    tick_volume: int

    real_volume: int | None = None
    spread: int | None = None