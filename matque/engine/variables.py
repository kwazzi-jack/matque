from matque.engine.core import *
from matque.engine.numerics import *
from matque.engine.operators import *


class Variable(Node):
    def __init__(self, name):
        self.name = name

    def to_latex(self):
        return self.name
