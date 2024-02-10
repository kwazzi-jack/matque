from matque.engine.core import *
from matque.engine.numerics import *
from matque.engine.variables import *


class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right


class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand


class Addition(BinaryOperator):
    def to_latex(self):
        return f"{self.left.to_latex()} + {self.right.to_latex()}"


class Multiplication(BinaryOperator):
    def __init__(self, left, right, explicit=False):
        super().__init__(left, right)
        self.explicit = explicit

    def to_latex(self):
        left_latex = self.left.to_latex()
        right_latex = self.right.to_latex()

        # Determine if the multiplication should be explicit based on the operands
        if self.explicit:
            return f"{left_latex} \\times {right_latex}"
        else:
            # Handle special cases for implicit multiplication
            if isinstance(self.left, Number) and isinstance(self.right, Variable):
                return f"{left_latex}{right_latex}"
            elif isinstance(self.left, Variable) and isinstance(self.right, Number):
                # Typically, variables are not prefixed by numbers without an operator in standard notation
                return f"{right_latex}{left_latex}"
            elif isinstance(self.left, Number) and isinstance(self.right, Number):
                # Numbers are typically explicitly multiplied
                return f"{left_latex} \\times {right_latex}"
            else:
                # Default to implicit multiplication for other cases
                return f"{left_latex} {right_latex}"


if __name__ == "__main__":
    # Example usage
    x = Variable("x")
    y = Variable("y")
    two = Number(2)
    three = Number(3)

    # Implicit multiplication
    expression1 = Multiplication(two, x)
    print(expression1.to_latex())  # Expected: 2x

    expression1 = Multiplication(x, two)
    print(expression1.to_latex())  # Expected: 2x

    # Explicit multiplication
    expression2 = Multiplication(x, y, explicit=True)
    print(expression2.to_latex())  # Expected: x \times y

    # Multiplication involving numbers only, treated as explicit
    expression3 = Multiplication(two, three)
    print(expression3.to_latex())  # Expected: 2 \times 3
