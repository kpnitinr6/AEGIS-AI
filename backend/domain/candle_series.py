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

    def first(self) -> Candle:
        """Return the first candle."""

        if not self._candles:
            raise ValueError("CandleSeries is empty")

        return self._candles[0]

    def latest(self) -> Candle:
        """Return the most recent candle."""
        if not self._candles:
            raise ValueError("CandleSeries is empty")

        return self._candles[-1]

    def previous(self) -> Candle:
        """Return the previous completed candle."""
        if len(self._candles) < 2:
            raise ValueError("CandleSeries contains fewer than two candles")

        return self._candles[-2]

    def __len__(self) -> int:
        return len(self._candles)

    def __iter__(self) -> Iterator[Candle]:
        return iter(self._candles)

    def is_empty(self) -> bool:
        """Return True if the series contains no candles."""
        return len(self._candles) == 0