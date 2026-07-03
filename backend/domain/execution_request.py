"""
AEGIS AI Domain

Immutable execution request.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal

from backend.domain.decision import DecisionAction
from backend.domain.instrument import Instrument
from backend.domain.timeframe import Timeframe


@dataclass(frozen=True, slots=True)
class ExecutionRequest:
    """
    Immutable request sent to an execution engine.

    This object represents the information required to
    execute a trading decision. It is intentionally
    independent of any broker or execution platform.
    """

    instrument: Instrument
    timeframe: Timeframe
    action: DecisionAction
    confidence: Decimal

    def __post_init__(self) -> None:

        if not isinstance(self.instrument, Instrument):
            raise TypeError(
                "instrument must be an Instrument"
            )

        if not isinstance(self.timeframe, Timeframe):
            raise TypeError(
                "timeframe must be a Timeframe"
            )

        if not isinstance(self.action, DecisionAction):
            raise TypeError(
                "action must be a DecisionAction"
            )

        if not isinstance(self.confidence, Decimal):
            raise TypeError(
                "confidence must be a Decimal"
            )