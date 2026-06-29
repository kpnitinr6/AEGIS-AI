"""
AEGIS AI Domain

Represents the structural interpretation of a confirmed market swing.
"""

from __future__ import annotations

from dataclasses import dataclass

from backend.domain.structure_type import StructureType
from backend.domain.swing import Swing


@dataclass(frozen=True, slots=True)
class StructurePoint:
    """
    Immutable value object representing the structural meaning
    of a confirmed market swing.
    """

    structure: StructureType
    swing: Swing

    def __post_init__(self) -> None:
        if not isinstance(self.structure, StructureType):
            raise TypeError("structure must be a StructureType")

        if not isinstance(self.swing, Swing):
            raise TypeError("swing must be a Swing")