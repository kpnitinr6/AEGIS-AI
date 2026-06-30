"""
AEGIS AI Domain

Immutable process result.
"""

from __future__ import annotations

from dataclasses import dataclass

from backend.domain.decision import Decision
from backend.domain.execution_result import ExecutionResult
from backend.domain.risk_assessment import RiskAssessment


@dataclass(
    frozen=True,
    slots=True,
)
class ProcessResult:
    """
    Represents the complete outcome of a single
    AEGIS processing cycle.

    A ProcessResult captures the decision,
    the outcome of risk evaluation,
    and the execution result (if any).
    """

    decision: Decision
    risk_assessment: RiskAssessment
    execution_result: ExecutionResult | None