"""
AEGIS AI Perception

Defines the contract for all perception detectors.
"""

from __future__ import annotations

from typing import Any, Protocol


class Detector(Protocol):
    """
    Contract implemented by every perception detector.

    A detector observes market data and produces
    domain facts.

    Detectors never:
    - produce trading evidence,
    - make decisions,
    - execute trades.
    """

    def detect(
        self,
        subject: Any,
    ) -> Any:
        """
        Detect domain facts from the supplied subject.
        """
        ...