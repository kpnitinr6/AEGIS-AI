"""
Replay demonstration using a bullish market scenario.
"""

from backend.application.factory import create_aegis
from backend.application.replay_engine import ReplayEngine
from backend.domain import Instrument, Timeframe
from backend.testing.scenarios.bullish_trend_scenario import BullishTrendScenario
from examples.shared.replay_console import print_replay


def main() -> None:
    aegis = create_aegis()
    replay_engine = ReplayEngine(application=aegis)

    series = BullishTrendScenario().generate(
        instrument=Instrument(code="XAUUSD", name="Gold Spot"),
        timeframe=Timeframe.M5,
        count=20,
    )

    print_replay(replay_engine.replay(series))


if __name__ == "__main__":
    main()
