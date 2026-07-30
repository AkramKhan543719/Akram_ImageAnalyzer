from abc import ABC, abstractmethod


class BaseAnalyzer(ABC):
    """Abstract Base Class for all analyzers."""

    @abstractmethod
    def analyze(self):
        pass

    @abstractmethod
    def generate_report(self):
        pass