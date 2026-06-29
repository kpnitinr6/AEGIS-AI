"""
AEGIS AI

Perception Layer
"""

from .structure_detector import StructureDetector
from .swing_detector import SwingDetector

__all__ = [
    "SwingDetector",
    "StructureDetector",
]