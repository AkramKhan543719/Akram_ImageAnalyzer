"""
report_generator.py

Demonstrates Runtime Polymorphism.
"""


class ReportGenerator:
    """
    Parent Class
    """

    def generate(self):
        print("Generating Report...")


class TextReport(ReportGenerator):
    """
    Child Class
    """

    def generate(self):
        print("Generating Text Report...")


class CSVReport(ReportGenerator):
    """
    Child Class
    """

    def generate(self):
        print("Generating CSV Report...")