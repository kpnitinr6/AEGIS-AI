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

    def add(
        self,
        candle: Candle,
    ) -> None:
        """Add a completed candle."""
        self._candles.append(candle)

    def first(self) -> Candle:
        """Return the first candle."""

        if not self._candles:
            raise ValueError(
                "CandleSeries is empty"
            )

        return self._candles[0]

    def latest(self) -> Candle:
        """Return the most recent candle."""

        if not self._candles:
            raise ValueError(
                "CandleSeries is empty"
            )

        return self._candles[-1]

    def previous(self) -> Candle:
        """Return the previous completed candle."""

        if len(self._candles) < 2:
            raise ValueError(
                "CandleSeries contains fewer than two candles"
            )

        return self._candles[-2]

    def previous_of(
        self,
        candle: Candle,
    ) -> Candle | None:
        """
        Return the candle immediately preceding the
        supplied candle.

        Returns None if the supplied candle is the
        first candle in the series.
        """

        for index, current in enumerate(
            self._candles,
        ):
            if current == candle:

                if index == 0:
                    return None

                return self._candles[index - 1]

        raise ValueError(
            "candle does not belong to this CandleSeries"
        )

    def candles_after(
        self,
        candle: Candle,
    ) -> list[Candle]:
        """
        Return every candle occurring after the
        supplied candle.
        """

        for index, current in enumerate(
            self._candles,
        ):
            if current == candle:
                return self._candles[index + 1 :]

        raise ValueError(
            "candle does not belong to this CandleSeries"
        )

    def __len__(self) -> int:
        return len(self._candles)

    def __iter__(self) -> Iterator[Candle]:
        return iter(self._candles)

    def is_empty(self) -> bool:
        """Return True if the series contains no candles."""
        return len(self._candles) == 0