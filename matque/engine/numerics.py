from matque.engine.core import *
from matque.engine.operators import *
from matque.engine.variables import *


class Number(Node):
    def __init__(self, value):
        self.value = value

    def to_latex(self):
        return str(self.value)
