"""
Tests for PerceptionResult.
"""

from backend.perception.perception_result import (
    PerceptionResult,
)


def test_default_perception_result() -> None:

    result = PerceptionResult()

    assert result.swings == []

    assert result.market_structure is None

    assert result.break_of_structures == []

    assert result.change_of_characters == []

    assert result.liquidity_sweeps == []

    assert result.order_blocks == []


def test_perception_result_is_immutable() -> None:

    result = PerceptionResult()

    try:
        result.swings = []
        assert False
    except AttributeError:
        pass