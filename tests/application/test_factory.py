"""
Tests for the AEGIS application factory.
"""

from backend.application import AEGIS
from backend.application.factory import create_aegis


def test_factory_creates_aegis() -> None:

    aegis = create_aegis()

    assert isinstance(
        aegis,
        AEGIS,
    )