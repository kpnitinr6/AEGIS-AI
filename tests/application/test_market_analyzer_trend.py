"""
Tests for MarketAnalyzer trend analysis.
"""

from datetime import datetime, timezone
from decimal import Decimal

from backend.application.market_analyzer import MarketAnalyzer
from backend.domain import (
    Candle,
    CandleSeries,
    Instrument,
    Time,
    Timeframe,
    TrendState,
)


def make_candle(
    *,
    high: str,
    low: str,
    close: str,
    minute: int,
) -> Candle:
    return Candle(
        instrument=Instrument(
            code="XAUUSD",
            name="Gold Spot",
        ),
        timeframe=Timeframe.M5,
        open_time=Time(
            datetime(
                2026,
                6,
                29,
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


def make_candle_series() -> CandleSeries:

    series = CandleSeries()

    series.add(
        make_candle(
            high="3350",
            low="3345",
            close="3348",
            minute=0,
        )
    )

    series.add(
        make_candle(
            high="3360",
            low="3348",
            close="3358",
            minute=5,
        )
    )

    series.add(
        make_candle(
            high="3352",
            low="3347",
            close="3350",
            minute=10,
        )
    )

    return series


def test_market_analyzer_populates_trend() -> None:

    analyzer = MarketAnalyzer()

    context = analyzer.analyze(
        make_candle_series(),
    )

    assert context.trend is not None
    assert context.trend.state == TrendState.BULLISH