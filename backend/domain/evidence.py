"""
AEGIS AI Domain

Represents a single piece of market evidence.
"""

from __future__ import annotations

from dataclasses import dataclass

from backend.domain.evidence_direction import EvidenceDirection
from backend.domain.evidence_source import EvidenceSource


@dataclass(frozen=True, slots=True)
class Evidence:
    """
    Immutable value object representing a single piece
    of evidence supporting market analysis.
    """

    source: EvidenceSource
    direction: EvidenceDirection
    reason: str

    def __post_init__(self) -> None:
        if not isinstance(self.source, EvidenceSource):
            raise TypeError(
                "source must be an EvidenceSource"
            )

        if not isinstance(
            self.direction,
            EvidenceDirection,
        ):
            raise TypeError(
                "direction must be an EvidenceDirection"
            )

        if not isinstance(self.reason, str):
            raise TypeError(
                "reason must be a string"
            )

        if not self.reason.strip():
            raise ValueError(
                "reason cannot be empty"
            )