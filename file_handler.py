"""
file_handler.py

Handles all file and folder operations.
"""

import os

from config import (
    INPUT_FOLDER,
    OUTPUT_FOLDER,
    LOG_FOLDER,
    REPORT_FOLDER,
    SUPPORTED_EXTENSIONS
)

from custom_exceptions import (
    UnsupportedFormatError
)


class FileHandler:
    """
    File Handler Class
    Demonstrates OOP
    """

    @staticmethod
    def create_directories():

        folders = [

            INPUT_FOLDER,

            OUTPUT_FOLDER,

            LOG_FOLDER,

            REPORT_FOLDER

        ]

        for folder in folders:

            os.makedirs(folder, exist_ok=True)

    # -------------------------------------------------

    @staticmethod
    def get_image_files():

        image_files = []

        try:

            files = os.listdir(INPUT_FOLDER)

            for file in files:

                extension = os.path.splitext(file)[1].lower()

                if extension in SUPPORTED_EXTENSIONS:

                    image_files.append(
                        os.path.join(
                            INPUT_FOLDER,
                            file
                        )
                    )

            return image_files

        except FileNotFoundError:

            print("Input Folder Not Found")

            return []

        except Exception as error:

            print(error)

            return []

    # -------------------------------------------------

    @staticmethod
    def is_supported_image(file_path):

        extension = os.path.splitext(
            file_path
        )[1].lower()

        if extension not in SUPPORTED_EXTENSIONS:

            raise UnsupportedFormatError(

                f"{extension} format not supported."

            )

        return True

    # -------------------------------------------------

    @staticmethod
    def get_file_size(file_path):

        size = os.path.getsize(file_path)

        return round(
            size / (1024 * 1024),
            2
        )


# =====================================================
# Wrapper Functions
# (Keeps existing project compatible)
# =====================================================

def create_directories():
    FileHandler.create_directories()


def get_image_files():
    return FileHandler.get_image_files()


def is_supported_image(file_path):
    return FileHandler.is_supported_image(file_path)


def get_file_size(file_path):
    return FileHandler.get_file_size(file_path)