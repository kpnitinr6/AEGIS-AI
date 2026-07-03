"""
AEGIS AI Testing

Range Scenario.
"""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from decimal import Decimal

from backend.domain import (
    Candle,
    CandleSeries,
    Instrument,
    Time,
    Timeframe,
)
from backend.testing.scenarios.base import (
    MarketScenario,
)


class RangeScenario(MarketScenario):
    """
    Produces a deterministic ranging market.

    Price oscillates around a central value without
    establishing a sustained trend.
    """

    def generate(
        self,
        instrument: Instrument,
        timeframe: Timeframe,
        count: int,
    ) -> CandleSeries:

        if not isinstance(instrument, Instrument):
            raise TypeError(
                "instrument must be an Instrument"
            )

        if not isinstance(timeframe, Timeframe):
            raise TypeError(
                "timeframe must be a Timeframe"
            )

        if not isinstance(count, int):
            raise TypeError(
                "count must be an int"
            )

        if count <= 0:
            raise ValueError(
                "count must be greater than zero"
            )

        series = CandleSeries()

        now = datetime.now(timezone.utc)

        base_price = Decimal("3300.00")

        offsets = [
            Decimal("0.00"),
            Decimal("2.00"),
            Decimal("-1.00"),
            Decimal("1.00"),
            Decimal("0.00"),
            Decimal("2.00"),
            Decimal("-2.00"),
            Decimal("1.00"),
        ]

        for index in range(count):

            price = base_price + offsets[
                index % len(offsets)
            ]

            candle = Candle(
                instrument=instrument,
                timeframe=timeframe,
                open_time=Time(
                    now + timedelta(
                        minutes=index * 5,
                    )
                ),
                open=price,
                high=price + Decimal("2.00"),
                low=price - Decimal("2.00"),
                close=price + Decimal("0.50"),
                tick_volume=1000 + index,
            )

            series.add(
                candle,
            )

        return series