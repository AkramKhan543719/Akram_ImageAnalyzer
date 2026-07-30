"""
utils.py

Contains helper functions used across the Image Analyzer project.
"""

import os
from math import gcd


# ------------------------------------------------------------
# File Related Functions
# ------------------------------------------------------------

def get_filename(file_path):
    """
    Returns only the filename.
    """

    return os.path.basename(file_path)


def get_extension(file_path):
    """
    Returns file extension.
    """

    return os.path.splitext(file_path)[1].lower()


# ------------------------------------------------------------
# Image Related Functions
# ------------------------------------------------------------

def format_resolution(width, height):
    """
    Returns formatted resolution.
    """

    return f"{width} x {height}"


def get_orientation(width, height):
    """
    Determines image orientation.
    """

    if width > height:
        return "Landscape"

    elif height > width:
        return "Portrait"

    else:
        return "Square"


def calculate_aspect_ratio(width, height):
    """
    Returns simplified aspect ratio.
    """

    value = gcd(width, height)

    return f"{width // value}:{height // value}"


def get_image_type(channels):
    """
    Determines image type.
    """

    if channels == 3:
        return "RGB"

    elif channels == 1:
        return "Grayscale"

    else:
        return "Unknown"


# ------------------------------------------------------------
# Console Printing Functions
# ------------------------------------------------------------

def print_line():
    """
    Prints separator line.
    """

    print("-" * 60)


def print_title(title):
    """
    Prints application title.
    """

    print()
    print("=" * 60)
    print(title.center(60))
    print("=" * 60)


def print_dataset_info(total_images):
    """
    Displays dataset information.
    """

    print()
    print("=" * 60)
    print("DATASET INFORMATION")
    print("=" * 60)

    print(f"Dataset Folder     : input_images")
    print(f"Supported Formats  : JPG | JPEG | PNG | BMP")
    print(f"Total Images Found : {total_images}")

    print("=" * 60)