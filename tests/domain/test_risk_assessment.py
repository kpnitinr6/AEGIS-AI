"""
Tests for the RiskAssessment domain model.
"""

from backend.domain.risk_assessment import RiskAssessment


def test_risk_assessment_approved() -> None:

    assessment = RiskAssessment(
        approved=True,
        reason="Risk accepted.",
    )

    assert assessment.approved is True
    assert assessment.reason == "Risk accepted."


def test_risk_assessment_rejected() -> None:

    assessment = RiskAssessment(
        approved=False,
        reason="Maximum daily loss exceeded.",
    )

    assert assessment.approved is False
    assert (
        assessment.reason
        == "Maximum daily loss exceeded."
    )