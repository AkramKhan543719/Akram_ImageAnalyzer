"""
config.py

This file contains all the constant values used in the project.
Keeping constants here improves modularity and makes maintenance easier.
"""

import os

# ----------------------------
# Project Paths
# ----------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INPUT_FOLDER = os.path.join(BASE_DIR, "input_images")
OUTPUT_FOLDER = os.path.join(BASE_DIR, "output_images")
LOG_FOLDER = os.path.join(BASE_DIR, "logs")
REPORT_FOLDER = os.path.join(BASE_DIR, "reports")

# ----------------------------
# Log File
# ----------------------------

LOG_FILE = os.path.join(LOG_FOLDER, "image_analyzer.log")

# ----------------------------
# Report File
# ----------------------------

REPORT_FILE = os.path.join(REPORT_FOLDER, "report.txt")

# ----------------------------
# Supported Image Formats
# ----------------------------

SUPPORTED_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".bmp"
}

# ----------------------------
# Resize Dimensions
# ----------------------------

RESIZE_WIDTH = 640
RESIZE_HEIGHT = 480