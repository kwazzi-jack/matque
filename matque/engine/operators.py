from matque.engine.core import Node
from matque.engine.numerics import Number
from matque.engine.variables import Variable


class BinaryOperator(Node):
    _to_string_operator = "!NaN!"
    _to_latex_operator = "!NaN!"

    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{self.__class__.__name__}[{self.left}, {self.right}]"

    def __str__(self):
        return f"{self.left}{self.__class__._to_string_operator}{self.right}"

    def to_latex(self):
        return f"{self.left.to_latex()} {self.__class__._to_latex_operator} {self.right.to_latex()}"


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand


class Addition(BinaryOperator):
    _to_string_operator = "+"
    _to_latex_operator = "+"


class Subtraction(BinaryOperator):
    _to_string_operator = "-"
    _to_latex_operator = "-"


class Multiplication(BinaryOperator):
    _to_string_operator = "*"
    _to_latex_operator = "\\times"


class Division(BinaryOperator):
    _to_string_operator = "/"
    _to_latex_operator = "*"


class Function(Node):
    def __init__(self, name, *args) -> None:
        self.name = name
        self.args = args

    def to_latex(self):
        args_latex = ", ".join(arg.to_latex() for arg in self.args)
        return f"{self.name}({args_latex})"


# Define operators


if __name__ == "__main__":
    # Example usage
    x = Variable("x")
    y = Variable("y")
    two = Number(2)
    three = Number(3)

    # Implicit multiplication
    expression1 = Multiplication(two, x)
    print(expression1, expression1.to_latex())  # Expected: 2x

    expression1 = Multiplication(x, two)
    print(expression1, expression1.to_latex())  # Expected: 2x

    # Explicit multiplication
    expression2 = Multiplication(x, y)
    print(expression2, expression2.to_latex())  # Expected: x \times y

    # Multiplication involving numbers only, treated as explicit
    expression3 = Multiplication(two, three)
    print(expression3, expression3.to_latex())  # Expected: 2 \times 3
