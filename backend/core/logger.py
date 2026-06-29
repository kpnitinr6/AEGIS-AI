"""
AEGIS AI Logger

Central logging configuration for the entire application.
"""

import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("AEGIS")