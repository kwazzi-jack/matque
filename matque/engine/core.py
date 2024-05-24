from abc import ABC, abstractmethod


class Node(ABC):
    @abstractmethod
    def to_latex(self):
        pass
