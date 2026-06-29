"""
AEGIS AI Services

Defines the base contract for all analyzers.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class Analyzer(ABC):
    """
    Base class for all AEGIS analyzers.

    An analyzer consumes immutable domain objects and
    derives higher-level domain knowledge.

    Analyzers must:
    - Never mutate domain objects.
    - Be deterministic.
    - Return domain objects.
    """

    @abstractmethod
    def analyze(self, subject: Any) -> Any:
        """
        Analyze a domain object and return derived knowledge.
        """
        raise NotImplementedError