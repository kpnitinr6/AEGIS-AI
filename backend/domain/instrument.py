"""
AEGIS AI Domain

Represents a market instrument.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Instrument:
    """
    Immutable market instrument.
    """

    code: str
    name: str

    def __post_init__(self) -> None:
        if not self.code.strip():
            raise ValueError("Instrument code cannot be empty")

        if not self.name.strip():
            raise ValueError("Instrument name cannot be empty")