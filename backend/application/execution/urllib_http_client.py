"""
AEGIS AI

Urllib HTTP client.
"""

from __future__ import annotations

import json
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from backend.application.execution.http_client import (
    HttpClient,
)


class UrllibHttpClient(HttpClient):
    """
    HTTP client implemented using urllib.
    """

    def post(
        self,
        url: str,
        payload: dict[str, str],
    ) -> dict:

        request = Request(
            url,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
            },
            method="POST",
        )

        with urlopen(request) as response:
            return json.loads(
                response.read().decode("utf-8")
            )