"""
AEGIS AI Domain

Immutable trade intent.
"""

from __future__ import annotations

from dataclasses import dataclass

from backend.domain.decision import Decision
from backend.domain.instrument import Instrument
from backend.domain.timeframe import Timeframe


@dataclass(frozen=True, slots=True)
class TradeIntent:
    """
    Represents the intention to execute a trading decision.

    A TradeIntent is independent of any broker or execution
    platform. It simply states that AEGIS intends to act on
    a particular instrument and timeframe based on a
    previously created Decision.
    """

    decision: Decision
    instrument: Instrument
    timeframe: Timeframe