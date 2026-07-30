"""
main.py

Entry Point of Image Analyzer Project
"""

import logging

from logger_config import setup_logger
from file_handler import create_directories
from image_analyzer import ImageAnalyzer

from report_generator import (
    TextReport,
    CSVReport
)

from utils import print_title


def main():
    """
    Main Function
    """

    try:

        # Configure Logger
        setup_logger()

        logging.info("Application Started")

        # Create Required Directories
        create_directories()

        # Display Project Title
        print_title("IMAGE ANALYZER")

        print("Welcome to Image Analyzer Project")
        print("Developed using Python + OpenCV")
        print()

        print(
            f"Project : {ImageAnalyzer.project_name()}"
        )

        print(
            f"Version : {ImageAnalyzer.project_version()}"
        )

        print()

        # Create Object
        analyzer = ImageAnalyzer()

        try:

            analyzer.analyze()

        except Exception as error:

            logging.exception(error)

            print(error)

        finally:

            print("\nImage Analysis Finished Successfully.")

        print()
        print("=" * 60)
        print("POLYMORPHISM DEMO")
        print("=" * 60)

        reports = [

            TextReport(),

            CSVReport()

        ]

        for report in reports:

            report.generate()

        print("=" * 60)

        logging.info(
            "Application Finished Successfully"
        )

    except Exception as error:

        logging.exception(error)

        print("\nUnexpected Error Occurred")

        print(error)


if __name__ == "__main__":
    main()