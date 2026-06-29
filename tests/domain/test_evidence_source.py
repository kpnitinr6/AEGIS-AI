"""
Tests for the EvidenceSource enumeration.
"""

from backend.domain import EvidenceSource


def test_break_of_structure_value() -> None:
    assert (
        EvidenceSource.BREAK_OF_STRUCTURE.value
        == "BREAK_OF_STRUCTURE"
    )


def test_change_of_character_value() -> None:
    assert (
        EvidenceSource.CHANGE_OF_CHARACTER.value
        == "CHANGE_OF_CHARACTER"
    )


def test_liquidity_sweep_value() -> None:
    assert (
        EvidenceSource.LIQUIDITY_SWEEP.value
        == "LIQUIDITY_SWEEP"
    )


def test_order_block_value() -> None:
    assert (
        EvidenceSource.ORDER_BLOCK.value
        == "ORDER_BLOCK"
    )


def test_fair_value_gap_value() -> None:
    assert (
        EvidenceSource.FAIR_VALUE_GAP.value
        == "FAIR_VALUE_GAP"
    )


def test_trend_value() -> None:
    assert (
        EvidenceSource.TREND.value
        == "TREND"
    )


def test_dow_theory_value() -> None:
    assert (
        EvidenceSource.DOW_THEORY.value
        == "DOW_THEORY"
    )


def test_wyckoff_value() -> None:
    assert (
        EvidenceSource.WYCKOFF.value
        == "WYCKOFF"
    )


def test_volume_value() -> None:
    assert (
        EvidenceSource.VOLUME.value
        == "VOLUME"
    )

def test_market_shift_value() -> None:
    assert (
        EvidenceSource.MARKET_SHIFT.value
        == "MARKET_SHIFT"
    )