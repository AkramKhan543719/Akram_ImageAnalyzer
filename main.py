"""
main.py

Entry point of the Image Analyzer Project.
"""

import logging

from logger_config import setup_logger
from file_handler import create_directories
from image_analyzer import ImageAnalyzer
from utils import print_title


def main():
    """
    Main function to start the Image Analyzer.
    """

    try:

        # Configure Logger
        setup_logger()

        logging.info("Application Started")

        # Create Required Directories
        create_directories()

        # Display Project Title
        print_title("IMAGE ANALYZER")

        print("Welcome to the Image Analyzer Project")
        print("Developed using Python + OpenCV")
        print()

        # Create Object
        analyzer = ImageAnalyzer()

        # Start Image Analysis
        analyzer.analyze_images()

        logging.info("Application Finished Successfully")

    except Exception as error:

        logging.exception(error)

        print("\nUnexpected Error Occurred")
        print(error)


if __name__ == "__main__":
    main()