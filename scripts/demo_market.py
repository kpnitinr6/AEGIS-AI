from backend.adapters.fake.adapter import FakeMarketAdapter
from backend.market.engine import MarketEngine
from backend.domain.timeframe import Timeframe


adapter = FakeMarketAdapter()

market = MarketEngine(adapter)

candles = market.get_candles(
    symbol="XAUUSD",
    timeframe=Timeframe.M15,
    count=5,
)

print()

print("AEGIS AI")
print("=" * 40)

for candle in candles:

    print(
        candle.timestamp,
        candle.close,
    )