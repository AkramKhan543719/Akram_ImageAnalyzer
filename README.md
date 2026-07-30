# Image Analyzer

## Description

Image Analyzer is a Python project that scans images from a folder, extracts image information, performs basic image processing, and generates a report.

---

## Features

- Read images from a folder
- Validate supported image formats
- Display image information
- Convert image to grayscale
- Resize image
- Save processed image
- Generate analysis report
- Logging
- Exception handling

---

## Supported Formats

- JPG
- JPEG
- PNG
- BMP

---

## Folder Structure

ImageAnalyzer/
│
├── main.py
├── image_analyzer.py
├── file_handler.py
├── logger_config.py
├── config.py
├── utils.py
│
├── input_images/
├── output_images/
├── logs/
├── reports/

---

## Requirements

- Python 3.x
- OpenCV
- NumPy

---

## Run

```bash
python main.py
```