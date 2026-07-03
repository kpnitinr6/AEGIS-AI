"""
AEGIS AI

Agent HTTP Client.
"""

from __future__ import annotations

import json
from urllib.request import urlopen


class AgentHttpClient:
    """
    Simple HTTP client used by the MT5 Agent
    to communicate with the AEGIS Bridge.
    """

    def __init__(
        self,
        base_url: str,
    ) -> None:

        if not base_url.strip():
            raise ValueError(
                "base_url cannot be empty"
            )

        self._base_url = base_url.rstrip("/")

    def get(
        self,
        endpoint: str,
    ) -> dict:

        if not endpoint.startswith("/"):
            raise ValueError(
                "endpoint must start with '/'"
            )

        url = (
            self._base_url
            + endpoint
        )

        with urlopen(url) as response:

            body = response.read()

        return json.loads(
            body.decode("utf-8")
        )