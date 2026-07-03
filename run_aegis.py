"""
AEGIS AI

Application entry point.
"""

from __future__ import annotations

from backend.adapters.fake import FakeMarketAdapter
from backend.application.application_service import (
    ApplicationService,
)
from backend.application.factory import (
    create_aegis,
)
from backend.application.process_result_presenter import (
    ProcessResultPresenter,
)
from backend.domain import (
    Instrument,
    Timeframe,
)


def main() -> None:

    print()
    print("=" * 60)
    print("AEGIS AI")
    print("Phase III - Living System")
    print("=" * 60)
    print()

    application = ApplicationService(
        adapter=FakeMarketAdapter(),
        aegis=create_aegis(),
    )

    presenter = ProcessResultPresenter()

    run_result = application.run(
        instrument=Instrument(
            code="XAUUSD",
            name="Gold Spot",
        ),
        timeframe=Timeframe.M5,
        candle_count=200,
    )

    print(
        presenter.present(
            run_result.context,
            run_result.result,
        )
    )


if __name__ == "__main__":
    main()