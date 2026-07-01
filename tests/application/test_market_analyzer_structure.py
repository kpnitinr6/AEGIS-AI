"""
Tests for MarketAnalyzer structure integration.
"""

from datetime import datetime, timezone
from decimal import Decimal

from backend.application.market_analyzer import MarketAnalyzer
from backend.domain import (
    Candle,
    Instrument,
    Time,
    Timeframe,
)


def make_candle(
    *,
    high: str,
    low: str,
    close: str,
    minute: int,
) -> Candle:

    instrument = Instrument(
        code="XAUUSD",
        name="Gold Spot",
    )

    return Candle(
        instrument=instrument,
        timeframe=Timeframe.M5,
        open_time=Time(
            datetime(
                2026,
                7,
                1,
                9,
                minute,
                tzinfo=timezone.utc,
            )
        ),
        open=Decimal(close),
        high=Decimal(high),
        low=Decimal(low),
        close=Decimal(close),
        tick_volume=100,
    )


def test_market_analyzer_builds_market_structure() -> None:

    analyzer = MarketAnalyzer()

    context = analyzer.analyze(
        [
            make_candle(
                high="3350",
                low="3345",
                close="3348",
                minute=0,
            ),
            make_candle(
                high="3360",
                low="3348",
                close="3358",
                minute=5,
            ),
            make_candle(
                high="3352",
                low="3347",
                close="3350",
                minute=10,
            ),
        ]
    )

    assert context.market_structure is not None

    assert len(context.market_structure) == 1