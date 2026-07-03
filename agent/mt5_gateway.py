"""
AEGIS AI

MT5 Gateway.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod


class MT5Gateway(ABC):
    """
    Abstract gateway responsible for all
    communication with MetaTrader 5.

    Every MT5 interaction must pass through
    this interface.
    """

    @abstractmethod
    def get_status(
        self,
    ) -> dict:
        """
        Return gateway status.
        """
        raise NotImplementedError

    @abstractmethod
    def get_candles(
        self,
        symbol: str,
        timeframe: str,
        count: int,
    ) -> dict:
        """
        Retrieve market candles.
        """
        raise NotImplementedError

    @abstractmethod
    def execute_order(
        self,
        payload: dict,
    ) -> dict:
        """
        Execute an order.
        """
        raise NotImplementedError

    @abstractmethod
    def get_account(
        self,
    ) -> dict:
        """
        Retrieve account information.
        """
        raise NotImplementedError

    @abstractmethod
    def get_positions(
        self,
    ) -> dict:
        """
        Retrieve open positions.
        """
        raise NotImplementedError