import math

from matque.engine.core import Node


class Number(Node):
    def __init__(self, value):
        self.value = value

    def to_latex(self):
        return str(self.value)

    def __str__(self) -> str:
        return str(self.value)


class MathConstant(Node):
    def __init__(self, name, symbol=None, value=None):
        self.name = name
        self.symbol = symbol or name
        self.value = value

    def to_latex(self):
        return self.symbol


if __name__ == "__main__":
    # Public Mathematical Constants
    pi = MathConstant("pi", "\pi", math.pi)
    e = MathConstant("e", math.e)
