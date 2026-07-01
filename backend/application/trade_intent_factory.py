"""
AEGIS AI

Trade Intent Factory.
"""

from __future__ import annotations

from backend.domain import (
    Decision,
    MarketContext,
    RiskAssessment,
    TradeIntent,
)


class TradeIntentFactory:
    """
    Creates TradeIntent objects after
    risk approval.
    """

    def create(
        self,
        *,
        context: MarketContext,
        decision: Decision,
        assessment: RiskAssessment,
    ) -> TradeIntent | None:

        if not assessment.approved:
            return None

        return TradeIntent(
            decision=decision,
            instrument=context.instrument,
            timeframe=context.timeframe,
        )