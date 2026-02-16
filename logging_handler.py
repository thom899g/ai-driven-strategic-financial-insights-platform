"""
This module provides a custom logging handler for the financial insights platform.

It sets up both file and console logging with appropriate formatting and log levels.
"""

import logging
from typing import Dict
import sys

class CustomLogger:
    """
    A class to handle custom logging configuration and setup.

    Attributes:
        logger: Instance of the logger for this module.
    """

    @staticmethod
    def setup_logger(name: str, level: int = logging.INFO) -> logging.Logger:
        """
        Sets up a logger with both file and console handlers.

        Args:
            name: Name of the logger.
            level: Logging level (default is INFO).

        Returns:
            Configured logger instance.
        """
        logger = logging.getLogger(name)
        logger.setLevel(level)

        # Prevent adding handlers multiple times
        if logger.handlers:
            return logger

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        # File handler
        file_handler = logging.FileHandler("financial_insights.log")
        file_handler.setFormatter