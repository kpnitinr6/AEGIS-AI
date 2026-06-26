"""
AEGIS AI Domain

Represents a collection of market candles.
"""

from collections.abc import Iterator

from backend.domain.candle import Candle


class CandleSeries:
    """
    A collection of completed market candles.

    Provides domain-specific methods instead of exposing
    raw list operations.
    """

    def __init__(self) -> None:
        self._candles: list[Candle] = []

    def add(self, candle: Candle) -> None:
        """Add a completed candle."""
        self._candles.append(candle)

    def latest(self) -> Candle:
        """Return the most recent candle."""
        return self._candles[-1]

    def previous(self) -> Candle:
        """Return the previous completed candle."""
        return self._candles[-2]

    def __len__(self) -> int:
        return len(self._candles)

    def __iter__(self) -> Iterator[Candle]:
        return iter(self._candles)