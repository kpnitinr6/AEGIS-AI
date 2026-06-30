"""
AEGIS AI Domain

Immutable execution result.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(
    frozen=True,
    slots=True,
)
class ExecutionResult:
    """
    Represents the outcome of an execution attempt.
    """

    success: bool
    message: str