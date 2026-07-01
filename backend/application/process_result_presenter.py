"""
AEGIS AI

Process Result Presenter.
"""

from __future__ import annotations

from backend.domain import (
    MarketContext,
    ProcessResult,
)


class ProcessResultPresenter:
    """
    Converts an application run into a human-readable summary.
    """

    def present(
        self,
        context: MarketContext,
        result: ProcessResult,
    ) -> str:

        market_structure = (
            context.market_structure.name
            if context.market_structure is not None
            else "Unknown"
        )

        trend = (
            context.trend.name
            if context.trend is not None
            else "Unknown"
        )

        execution = (
            result.execution_result.message
            if result.execution_result is not None
            else "Not executed."
        )

        return (
            "========================================\n"
            "               AEGIS AI\n"
            "========================================\n"
            "\n"
            f"Instrument        : {context.instrument.code}\n"
            f"Timeframe         : {context.timeframe.name}\n"
            "\n"
            f"Market Structure  : {market_structure}\n"
            f"Trend             : {trend}\n"
            "\n"
            f"Decision          : {result.decision.action.name}\n"
            f"Confidence        : {result.decision.confidence}\n"
            "\n"
            f"Risk              : {result.risk_assessment.reason}\n"
            f"Execution         : {execution}\n"
            "\n"
            "========================================"
        )