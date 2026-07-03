"""
AEGIS AI

HTTP Client contract.
"""

from __future__ import annotations

from typing import Protocol


class HttpClient(Protocol):
    """
    Contract implemented by HTTP clients.
    """

    def post(
        self,
        url: str,
        payload: dict[str, str],
    ) -> dict:
        """
        Send a JSON payload and return the JSON response.
        """
        ...