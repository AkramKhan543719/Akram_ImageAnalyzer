"""
file_handler.py

Handles all file and folder operations for the Image Analyzer project.
"""

import os
from config import (
    INPUT_FOLDER,
    OUTPUT_FOLDER,
    LOG_FOLDER,
    REPORT_FOLDER,
    SUPPORTED_EXTENSIONS
)


def create_directories():
    """
    Create required project folders if they don't exist.
    """
    folders = [
        INPUT_FOLDER,
        OUTPUT_FOLDER,
        LOG_FOLDER,
        REPORT_FOLDER
    ]

    for folder in folders:
        os.makedirs(folder, exist_ok=True)


def get_image_files():
    """
    Returns a list of valid image file paths from the input folder.
    """

    image_files = []

    try:
        files = os.listdir(INPUT_FOLDER)

        for file in files:
            extension = os.path.splitext(file)[1].lower()

            if extension in SUPPORTED_EXTENSIONS:
                image_files.append(os.path.join(INPUT_FOLDER, file))

        return image_files

    except FileNotFoundError:
        print("Input folder not found.")
        return []

    except Exception as error:
        print(f"Error reading folder : {error}")
        return []


def is_supported_image(file_path):
    """
    Checks whether the file has a supported image extension.
    """

    extension = os.path.splitext(file_path)[1].lower()

    return extension in SUPPORTED_EXTENSIONS


def get_file_size(file_path):
    """
    Returns file size in MB.
    """

    size = os.path.getsize(file_path)

    return round(size / (1024 * 1024), 2)