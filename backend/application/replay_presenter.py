"""
AEGIS AI

Replay Presenter.
"""

from __future__ import annotations

from backend.application.application_run_result import (
    ApplicationRunResult,
)


class ReplayPresenter:
    """
    Presents one replay step in a human-readable form.
    """

    def present(
        self,
        run: ApplicationRunResult,
    ) -> str:

        context = run.context
        result = run.result

        trend = (
            context.trend.state.name
            if context.trend is not None
            else "UNKNOWN"
        )

        if context.market_structure is None:

            structure = "UNKNOWN"

        else:

            latest = context.market_structure.latest()

            if latest is None:
                structure = "EMPTY"
            else:
                structure = latest.structure.name

        lines = [
            "=" * 70,
            f"Instrument          : {context.instrument.code}",
            f"Timeframe           : {context.timeframe.name}",
            "",
            f"Trend               : {trend}",
            f"Latest Structure    : {structure}",
            "",
            "Market Events",
            "-" * 70,
            (
                "Break Of Structure  : "
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
            "Decision",
            "-" * 70,
            (
                "Action              : "
                f"{result.decision.action.name}"
            ),
            (
                "Confidence          : "
                f"{result.decision.confidence}"
            ),
            (
                "Evidence Count      : "
                f"{len(result.decision.evidence)}"
            ),
            "",
            "Evidence",
            "-" * 70,
        ]

        if result.decision.evidence:

            for evidence in result.decision.evidence:
                lines.append(
                    f"• [{evidence.source.name}] "
                    f"{evidence.reason}"
                )

        else:
            lines.append(
                "No evidence generated."
            )

        lines.extend(
            [
                "",
                "Risk",
                "-" * 70,
                result.risk_assessment.reason,
            ]
        )

        if result.execution_result is not None:

            lines.extend(
                [
                    "",
                    "Execution",
                    "-" * 70,
                    result.execution_result.message,
                ]
            )

        return "\n".join(lines)