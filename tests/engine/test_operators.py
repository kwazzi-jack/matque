import pytest

from matque.engine.numerics import Number, e, pi
from matque.engine.operators import Addition, Function, Multiplication
from matque.engine.variables import Variable


@pytest.mark.parametrize(
    "expression, expected_latex",
    [
        # Existing tests...
        # Function application with multiple arguments
        (Function("f", Number(2), Variable("x")), "f(2, x)"),
        # Constants in expressions
        (Multiplication(pi, Variable("x")), "\\pi x"),
        (Multiplication(Number(2), pi), "2\\pi"),
        (Addition(e, Multiplication(Number(2), pi)), "e + 2\\pi"),
        # Implicit multiplication with constants and variables
        (Multiplication(pi, e), "\\pi e"),
        (Multiplication(e, pi, explicit=True), "e \\times \\pi"),
        # Nested expressions
        (
            Addition(
                Multiplication(Number(2), Variable("x")),
                Multiplication(Number(3), Variable("y")),
            ),
            "2x + 3y",
        ),
        (
            Multiplication(Addition(Number(2), Variable("x")), Variable("y")),
            "(2 + x) y",
        ),
        # Edge cases
        (Addition(Number(0), e), "e"),  # Adding zero
        (
            Multiplication(Number(1), Function("sin", Variable("x"))),
            "sin(x)",
        ),  # Multiplying by one
        # Error handling (assuming your system might eventually handle errors or validation)
        # This test assumes your system would wrap or flag invalid operations somehow
        # (Function("sin", "invalid"), "Error: Invalid argument for sin"),  # Invalid argument type, if you decide to validate argument types
        # Simplification cases (if simplification logic is to be tested)
        # (Addition(Variable("x"), UnaryOperator("-", Variable("x"))), "0"),  # Simplifying to zero, if unary operators are implemented
    ],
)
def test_expression_to_latex(expression, expected_latex):
    assert expression.to_latex() == expected_latex, f"Failed to render correctly"
