"""
This module contains configuration settings for the financial insights platform.

It includes API keys, data sources, and other necessary configurations.
Configuration is loaded from environment variables or a YAML file.
"""

import os
from typing import Dict

class Configuration:
    """
    A class to manage configuration settings for the application.

    Attributes:
        config: Dictionary containing all configuration parameters.
    """

    def __init__(self) -> None:
        self.config = self._load_config()

    def _load_config(self) -> Dict:
        """
        Loads configuration from environment variables or a YAML file.

        Returns:
            Configuration dictionary.
        """
        try:
            config = {
                "API_KEY": os.getenv("FIN_API_KEY"),
                "DATA_SOURCES": ["alpha_vantage", "yahoo"],
                "MODEL_PATH": "models/stock_predictor.h5"
            }
            self._validate_config(config)
            return config
        except Exception as e:
            raise ConfigurationError(f"Failed to load configuration: {str(e)}")

    def _validate_config(self, config: Dict) -> None:
        """
        Validates the configuration dictionary.

        Args:
            config: Configuration dictionary to validate.
        """
        required_keys = ["API_KEY", "DATA_SOURCES"]
        missing_keys = [key for key in required_keys if key not in config]
        if missing_keys:
            raise ValueError(f"Missing required keys: {', '.join(missing_keys)}")

    def get(self, key: str) -> Optional[str]:
        """
        Retrieves a configuration value by key.

        Args:
            key: Configuration key to retrieve.

        Returns:
            Value of the configuration key if found; otherwise None.
        """
        return self.config.get(key)

class ConfigurationError(Exception):
    pass