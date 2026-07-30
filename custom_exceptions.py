class ImageAnalyzerError(Exception):
    """Base exception for Image Analyzer."""
    pass


class InvalidImageError(ImageAnalyzerError):
    """Raised when the image cannot be loaded."""
    pass


class UnsupportedFormatError(ImageAnalyzerError):
    """Raised when image format is not supported."""
    pass