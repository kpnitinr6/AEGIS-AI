"""
AEGIS AI

Historical Market Adapter.

Reads historical market data from a CSV file and converts it
into AEGIS domain objects.
"""

from __future__ import annotations

import csv
from datetime import datetime
from decimal import Decimal
from pathlib import Path
from backend.adapters.base import MarketAdapter
from backend.domain import (
    Candle,
    CandleSeries,
    Instrument,
    Time,
    Timeframe,
)


class HistoricalMarketAdapter(MarketAdapter):
    """
    Market adapter that loads historical candles from a CSV file.
    """

    REQUIRED_COLUMNS = (
        "timestamp",
        "open",
        "high",
        "low",
        "close",
        "tick_volume",
    )

    def __init__(self, csv_path: str | Path) -> None:
        self._csv_path = Path(csv_path)

    def get_candles(
        self,
        instrument: Instrument,
        timeframe: Timeframe,
        count: int,
    ) -> CandleSeries:

        if count <= 0:
            raise ValueError("count must be greater than zero")

        series = CandleSeries()

        with self._csv_path.open(
            "r",
            encoding="utf-8",
            newline="",
        ) as csv_file:

            reader = csv.DictReader(csv_file)

            if reader.fieldnames is None:
                raise ValueError("CSV file is missing a header row")

            missing = [
                column
                for column in self.REQUIRED_COLUMNS
                if column not in reader.fieldnames
            ]

            if missing:
                raise ValueError(
                    f"Missing required columns: {', '.join(missing)}"
                )

            rows = list(reader)

        if count < len(rows):
            rows = rows[-count:]

        for row in rows:
            timestamp = row["timestamp"].replace("Z", "+00:00")

            candle = Candle(
                instrument=instrument,
                timeframe=timeframe,
                open_time=Time(
                    datetime.fromisoformat(timestamp)
                ),
                open=Decimal(row["open"]),
                high=Decimal(row["high"]),
                low=Decimal(row["low"]),
                close=Decimal(row["close"]),
                tick_volume=int(row["tick_volume"]),
                real_volume=(
                    int(row["real_volume"])
                    if row.get("real_volume")
                    else None
                ),
                spread=(
                    int(row["spread"])
                    if row.get("spread")
                    else None
                ),
            )

            series.add(candle)

        return series
