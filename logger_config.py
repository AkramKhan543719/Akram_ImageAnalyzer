"""
logger_config.py

Configures logging for the Image Analyzer project.
"""

import logging
import os
from config import LOG_FOLDER, LOG_FILE


def setup_logger():
    """
    Creates log folder (if needed) and configures logging.
    """

    os.makedirs(LOG_FOLDER, exist_ok=True)

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s"
    )

    return logging.getLogger()