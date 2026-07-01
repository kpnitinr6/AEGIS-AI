"""
Integration tests for DecisionEngine with multiple reasoners.
"""

from datetime import datetime, timezone
from decimal import Decimal

from backend.application.decision_engine import DecisionEngine
from backend.domain import (
    BreakOfStructure,
    Candle,
    Instrument,
    MarketContext,
    MarketStructure,
    Price,
    StructurePoint,
    StructureType,
    Swing,
    SwingType,
    Time,
    Timeframe,
    Trend,
    TrendState,
)
from backend.domain.decision import DecisionAction
from backend.domain.policies.majority_vote_policy import (
    MajorityVotePolicy,
)
from backend.reasoning import (
    BOSReasoner,
    StructureReasoner,
    TrendReasoner,
)


def make_instrument() -> Instrument:
    return Instrument(
        code="XAUUSD",
        name="Gold Spot",
    )


def make_candle() -> Candle:
    return Candle(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        open_time=Time(
            datetime(
                2026,
                7,
                4,
                9,
                0,
                tzinfo=timezone.utc,
            )
        ),
        open=Decimal("3350"),
        high=Decimal("3360"),
        low=Decimal("3340"),
        close=Decimal("3355"),
        tick_volume=100,
    )


def make_market_structure() -> MarketStructure:

    structure = MarketStructure(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
    )

    structure.append(
        StructurePoint(
            structure=StructureType.HIGHER_HIGH,
            swing=Swing(
                candle=make_candle(),
                type=SwingType.HIGH,
            ),
        )
    )

    return structure


def make_bos(
    structure: MarketStructure,
) -> BreakOfStructure:

    candle = make_candle()

    return BreakOfStructure(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        broken_structure=structure.latest(),
        confirming_candle=candle,
        break_price=Price(
            instrument=make_instrument(),
            amount=candle.close,
            time=candle.open_time,
        ),
    )


def test_multiple_reasoners_produce_buy_decision() -> None:

    market_structure = make_market_structure()

    context = MarketContext(
        instrument=make_instrument(),
        timeframe=Timeframe.M5,
        market_structure=market_structure,
        trend=Trend(
            state=TrendState.BULLISH,
            market_structure=market_structure,
        ),
        break_of_structures=[
            make_bos(
                market_structure,
            )
        ],
    )

    engine = DecisionEngine(
        reasoners=[
            TrendReasoner(),
            StructureReasoner(),
            BOSReasoner(),
        ],
        policy=MajorityVotePolicy(),
    )

    decision = engine.decide(context)

    assert decision.action == DecisionAction.BUY
    assert len(decision.evidence) == 3
    assert decision.confidence == Decimal("1.00")