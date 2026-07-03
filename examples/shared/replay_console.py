"""
Shared console presentation helpers for replay examples.
"""

from backend.application.application_run_result import ApplicationRunResult


def print_replay(results: list[ApplicationRunResult]) -> None:
    print()
    print("=" * 70)
    print("AEGIS REPLAY DIAGNOSTICS")
    print("=" * 70)

    for index, run in enumerate(results, start=2):
        context = run.context
        process = run.result
        decision = process.decision

        print()
        print("=" * 70)
        print(f"STEP {index:02d}")
        print("=" * 70)

        print(f"Instrument          : {context.instrument.code}")
        print(f"Timeframe           : {context.timeframe.name}")

        trend = (
            context.trend.state.name
            if context.trend is not None
            else "UNKNOWN"
        )

        if (
            context.market_structure is not None
            and context.market_structure.latest() is not None
        ):
            structure = context.market_structure.latest().structure.name
        else:
            structure = "UNKNOWN"

        print(f"Trend               : {trend}")
        print(f"Market Structure    : {structure}")

        print()
        print("Market Events")
        print("-" * 70)
        print(f"Break Of Structure  : {len(context.break_of_structures)}")
        print(f"CHOCH               : {len(context.change_of_characters)}")
        print(f"Liquidity Sweeps    : {len(context.liquidity_sweeps)}")
        print(f"Order Blocks        : {len(context.order_blocks)}")

        print()
        print("Decision")
        print("-" * 70)
        print(f"Action              : {decision.action.name}")
        print(f"Confidence          : {decision.confidence}")
        print(f"Evidence Count      : {len(decision.evidence)}")

        print()
        print("Evidence")
        print("-" * 70)

        if decision.evidence:
            for evidence in decision.evidence:
                print(f"• [{evidence.source.name}] {evidence.reason}")
        else:
            print("No evidence generated.")

        print()
        print("Risk")
        print("-" * 70)
        print(process.risk_assessment.reason)

        if process.execution_result is not None:
            print()
            print("Execution")
            print("-" * 70)
            print(process.execution_result.message)

    print()
    print("=" * 70)
    print("Replay Complete")
    print("=" * 70)
