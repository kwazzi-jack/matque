from matque.engine.core import Node


class Variable(Node):
    def __init__(self, name):
        self.name = name

    def to_latex(self):
        return self.name

    def __str__(self) -> str:
        return self.name
