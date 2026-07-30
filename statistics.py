"""
statistics.py

Provides image statistics.
"""


class ImageStatistics:
    """
    Utility class for image statistics.
    """

    @staticmethod
    def calculate_pixels(width, height):
        """
        Returns total number of pixels.
        """
        return width * height

    @staticmethod
    def megapixels(width, height):
        """
        Returns megapixels.
        """
        return round(
            (width * height) / 1000000,
            2
        )

    @staticmethod
    def aspect(width, height):
        """
        Returns width-height ratio.
        """
        return round(
            width / height,
            2
        )