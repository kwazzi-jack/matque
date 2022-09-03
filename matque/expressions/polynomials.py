from calendar import c
from matque.expressions import Expression
from omegaconf import open_dict
from sympy import sympify, Symbol
from abc import ABC, abstractclassmethod
from typing import Union


class Polynomial(Expression, ABC):
    """
    General polynomial object
    """

    def __init__(self, **options):

        # Initialize Expression, no options
        super().__init__()

        # Default options
        defaults = {"class": "Polynomial", "mtype": "expression"}

        # Update with new options, note lock
        with open_dict(self.options):
            self.options.update(defaults)
            self.options.update(options)

        # Expression for Polynomial
        # TODO: Fix with proper implementation
        self.expr = None

    @property
    @abstractclassmethod
    def x_intercepts(self):
        pass

    @property
    def y_intercept(self):
        return self.expr.subs(self.x, 0)

    @property
    def intercepts(self):
        return self.x_intercepts, self.y_intercept

    @property
    def turn_points(self):
        pass

    @property
    def parity(self):
        pass

    def __str__(self) -> str:
        return str(self.expr)


class Linear(Polynomial):
    """
    Polynomial of degree=1
    """

    def __init__(self, a="a", b="b", x="x", **options):

        # Initialize Polynomial, no options
        super().__init__()

        # Set linear components
        self.a = Symbol(a)
        self.b = Symbol(b)
        self.x = Symbol(x)

        # Default options
        defaults = {"class": "Linear"}

        # Update with new options, note lock
        with open_dict(self.options):
            self.options.update(defaults)
            self.options.update(options)

        # Create expressions
        self.change(a, b, x)

    @property
    def x_intercepts(self):
        return -self.b / self.a

    def change(self, a="a", b="b", x="x"):
        """
        Change the terms of the linear polynomial
        based on the given inputs. Also acts as
        a reset of terms.

        Parameters
        ----------
        a : str, optional
            scale/gradient term of linear polynomial, by default "a"
        b : str, optional
            shift/y-int term of linear polynomial, by default "b"
        x : str, optional
            independent term of linear polynomial, by default "x"
        """

        self.a = Symbol(a)
        self.b = Symbol(b)
        self.x = Symbol(x)
        self.expr = sympify(f"{a} * {x} + {b}")


class Quadratic(Polynomial):
    """
    Polynomial of degree=2
    """

    pass


class Cubic(Polynomial):
    """
    Polynomial of degree=2
    """

    pass


if __name__ == "__main__":
    line = Linear()
    print(line)
    print(line.y_intercept)
    print(line.x_intercepts)
    print(line.change("1", "2"))
