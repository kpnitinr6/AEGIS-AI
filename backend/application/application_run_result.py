"""
AEGIS AI

Application Run Result.
"""

from __future__ import annotations

from dataclasses import dataclass

from backend.domain import (
    MarketContext,
    ProcessResult,
)


@dataclass(frozen=True, slots=True)
class ApplicationRunResult:
    """
    Result produced by one complete application run.
    """

    context: MarketContext
    result: ProcessResult