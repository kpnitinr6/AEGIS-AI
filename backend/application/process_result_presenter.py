"""
AEGIS AI

Process Result Presenter.
"""

from __future__ import annotations

from backend.domain import (
    Evidence,
    EvidenceSource,
    MarketContext,
    ProcessResult,
)


class ProcessResultPresenter:
    """
    Converts an application run into a human-readable summary.
    """

    _ORDER: dict[EvidenceSource, int] = {
        EvidenceSource.TREND: 1,
        EvidenceSource.STRUCTURE: 2,
        EvidenceSource.BREAK_OF_STRUCTURE: 3,
        EvidenceSource.CHANGE_OF_CHARACTER: 4,
        EvidenceSource.LIQUIDITY_SWEEP: 5,
    }

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

        lines = [
            "========================================",
            "               AEGIS AI",
            "========================================",
            "",
            f"Instrument        : {context.instrument.code}",
            f"Timeframe         : {context.timeframe.name}",
            "",
            f"Market Structure  : {market_structure}",
            f"Trend             : {trend}",
            "",
            "Market Understanding",
            "----------------------------------------",
            (
                "Break of Structures : "
                f"{len(context.break_of_structures)}"
            ),
            (
                "CHOCH               : "
                f"{len(context.change_of_characters)}"
            ),
            (
                "Liquidity Sweeps    : "
                f"{len(context.liquidity_sweeps)}"
            ),
            (
                "Order Blocks        : "
                f"{len(context.order_blocks)}"
            ),
            "",
            "",
            f"Decision          : {result.decision.action.name}",
            f"Confidence        : {result.decision.confidence}",
            "",
            "Evidence",
            "----------------------------------------",
        ]

        if result.decision.evidence:

            ordered = sorted(
                result.decision.evidence,
                key=self._evidence_sort_key,
            )

            for item in ordered:
                lines.append(f"• {item.reason}")

        else:
            lines.append(
                "No supporting evidence."
            )

        lines.extend(
            [
                "",
                f"Risk              : {result.risk_assessment.reason}",
                f"Execution         : {execution}",
                "",
                "========================================",
            ]
        )

        return "\n".join(lines)

    def _evidence_sort_key(
        self,
        evidence: Evidence,
    ) -> int:

        return self._ORDER.get(
            evidence.source,
            999,
        )