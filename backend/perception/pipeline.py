"""
AEGIS AI

Perception Pipeline.

Coordinates perception detectors and produces a
single immutable PerceptionResult from raw market
data.
"""

from __future__ import annotations

from backend.domain import CandleSeries
from backend.perception.break_of_structure_detector import (
    BreakOfStructureDetector,
)
from backend.perception.change_of_character_detector import (
    ChangeOfCharacterDetector,
)
from backend.perception.liquidity_sweep_detector import (
    LiquiditySweepDetector,
)
from backend.perception.order_block_detector import (
    OrderBlockDetector,
)
from backend.perception.perception_result import (
    PerceptionResult,
)
from backend.perception.structure_detector import (
    StructureDetector,
)
from backend.perception.swing_detector import (
    SwingDetector,
)


class PerceptionPipeline:
    """
    Coordinates the perception layer.

    Version 5

    Pipeline

        CandleSeries
            ↓
        SwingDetector
            ↓
        StructureDetector
            ├──────────────┬────────────────┐
            ▼              ▼                ▼
        BOS Detector   CHOCH Detector   Liquidity Sweep
            │
            ▼
     Order Block Detector
            │
            ▼
      PerceptionResult
    """

    def __init__(
        self,
        swing_detector: SwingDetector | None = None,
        structure_detector: StructureDetector | None = None,
        break_of_structure_detector: (
            BreakOfStructureDetector | None
        ) = None,
        change_of_character_detector: (
            ChangeOfCharacterDetector | None
        ) = None,
        liquidity_sweep_detector: (
            LiquiditySweepDetector | None
        ) = None,
        order_block_detector: (
            OrderBlockDetector | None
        ) = None,
    ) -> None:

        self._swing_detector = (
            swing_detector
            if swing_detector is not None
            else SwingDetector()
        )

        self._structure_detector = (
            structure_detector
            if structure_detector is not None
            else StructureDetector()
        )

        self._bos_detector = (
            break_of_structure_detector
            if break_of_structure_detector is not None
            else BreakOfStructureDetector()
        )

        self._choch_detector = (
            change_of_character_detector
            if change_of_character_detector is not None
            else ChangeOfCharacterDetector()
        )

        self._liquidity_detector = (
            liquidity_sweep_detector
            if liquidity_sweep_detector is not None
            else LiquiditySweepDetector()
        )

        self._order_block_detector = (
            order_block_detector
            if order_block_detector is not None
            else OrderBlockDetector()
        )

    def detect(
        self,
        candle_series: CandleSeries,
    ) -> PerceptionResult:

        if not isinstance(
            candle_series,
            CandleSeries,
        ):
            raise TypeError(
                "candle_series must be a CandleSeries"
            )

        swings = self._swing_detector.detect(
            candle_series,
        )

        if not swings:
            return PerceptionResult()

        market_structure = (
            self._structure_detector.detect(
                swings,
            )
        )

        break_of_structures = []

        bos = self._bos_detector.detect(
            market_structure,
        )

        if bos is not None:
            break_of_structures.append(
                bos,
            )

        change_of_characters = []

        choch = self._choch_detector.detect(
            market_structure,
        )

        if choch is not None:
            change_of_characters.append(
                choch,
            )

        liquidity_sweeps = (
            self._liquidity_detector.detect(
                swings,
                candle_series,
            )
        )

        order_blocks = []

        for bos in break_of_structures:

            order_block = (
                self._order_block_detector.detect(
                    candle_series,
                    bos,
                )
            )

            if order_block is not None:
                order_blocks.append(
                    order_block,
                )

        return PerceptionResult(
            swings=swings,
            market_structure=market_structure,
            break_of_structures=break_of_structures,
            change_of_characters=change_of_characters,
            liquidity_sweeps=liquidity_sweeps,
            order_blocks=order_blocks,
        )