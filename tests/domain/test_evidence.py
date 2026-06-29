"""
Tests for the Evidence domain object.
"""

from dataclasses import FrozenInstanceError

import pytest

from backend.domain import (
    Evidence,
    EvidenceDirection,
    EvidenceSource,
)


def test_create_valid_evidence() -> None:
    evidence = Evidence(
        source=EvidenceSource.STRUCTURE,
        direction=EvidenceDirection.BULLISH,
        reason="Higher High",
    )

    assert evidence.source == EvidenceSource.STRUCTURE
    assert evidence.direction == EvidenceDirection.BULLISH
    assert evidence.reason == "Higher High"


def test_invalid_source() -> None:
    with pytest.raises(TypeError):
        Evidence(
            source="STRUCTURE",
            direction=EvidenceDirection.BULLISH,
            reason="Higher High",
        )


def test_invalid_direction() -> None:
    with pytest.raises(TypeError):
        Evidence(
            source=EvidenceSource.STRUCTURE,
            direction="BULLISH",
            reason="Higher High",
        )


def test_invalid_reason_type() -> None:
    with pytest.raises(TypeError):
        Evidence(
            source=EvidenceSource.STRUCTURE,
            direction=EvidenceDirection.BULLISH,
            reason=123,
        )


def test_empty_reason() -> None:
    with pytest.raises(ValueError):
        Evidence(
            source=EvidenceSource.STRUCTURE,
            direction=EvidenceDirection.BULLISH,
            reason="   ",
        )


def test_evidence_is_immutable() -> None:
    evidence = Evidence(
        source=EvidenceSource.STRUCTURE,
        direction=EvidenceDirection.BULLISH,
        reason="Higher High",
    )

    with pytest.raises(FrozenInstanceError):
        evidence.reason = "Lower Low"