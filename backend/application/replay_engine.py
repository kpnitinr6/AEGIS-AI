"""
AEGIS AI

Replay Engine.

Replays a CandleSeries through the AEGIS application,
producing one ApplicationRunResult for each point
in time.
"""

from __future__ import annotations

from backend.application.aegis import AEGIS
from backend.application.application_run_result import (
    ApplicationRunResult,
)
from backend.domain import CandleSeries


class ReplayEngine:
    """
    Replays historical candles through AEGIS.
    """

    def __init__(
        self,
        application: AEGIS,
    ) -> None:

        self._application = application

    def replay(
        self,
        candle_series: CandleSeries,
    ) -> list[ApplicationRunResult]:

        if not isinstance(
            candle_series,
            CandleSeries,
        ):
            raise TypeError(
                "candle_series must be a CandleSeries"
            )

        results: list[
            ApplicationRunResult
        ] = []

        partial = CandleSeries()

        for candle in candle_series:

            partial.add(candle)

            if len(partial) < 2:
                continue

            results.append(
                self._application.process(partial)
            )

        return results