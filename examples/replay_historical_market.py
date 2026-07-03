"""
Replay demonstration using historical market data.
"""

from pathlib import Path

from backend.adapters.historical.adapter import HistoricalMarketAdapter
from backend.application.factory import create_aegis
from backend.application.replay_engine import ReplayEngine
from backend.domain import Instrument, Timeframe
from examples.shared.replay_console import print_replay


def main() -> None:
    adapter = HistoricalMarketAdapter(
        Path("datasets/sample/sample_gold_m5.csv")
    )

    series = adapter.get_candles(
        instrument=Instrument(code="XAUUSD", name="Gold Spot"),
        timeframe=Timeframe.M5,
        count=3,
    )

    replay_engine = ReplayEngine(application=create_aegis())
    print_replay(replay_engine.replay(series))


if __name__ == "__main__":
    main()
