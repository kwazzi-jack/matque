from matque.expressions import Expression
from matque.core.objects import Coord
from omegaconf import open_dict
from sympy import sympify, Symbol
from sympy.core.numbers import Integer, Float
import sympy as sp
from abc import ABC, abstractclassmethod
from collections.abc import Iterable
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

    # Properties
    @property
    @abstractclassmethod
    def parity(self):
        pass

    @property
    @abstractclassmethod
    def lead(self):
        pass

    @property
    @abstractclassmethod
    def const(self):
        pass

    @property
    @abstractclassmethod
    def terms(self):
        pass

    @property
    @abstractclassmethod
    def coeff(self):
        pass
    
    # Methods
    @abstractclassmethod
    def change(self):
        pass

    @abstractclassmethod
    def derive(self):
        pass

    @abstractclassmethod
    def factorise(self):
        pass

    def evaluate(self, *values):
        if len(values): 
            return [self.expr.subs(self.x, value) 
                        for value in values if not isinstance(value, Iterable)]
        elif isinstance(values, Iterable):
            return [self.expr.subs(self.x, value) for value in values]
        else:
            #TODO
            raise ValueError("TODO")
    
    # Dunders
    @abstractclassmethod
    def __str__(self):
        pass


class Linear(Polynomial):
    """
    Polynomial of degree=1
    """

    def __init__(self, a="a", b="b", x="x", **options):

        # Initialize Polynomial, no options
        super().__init__()

        # Default options
        defaults = {"class": "Linear"}

        # Update with new options, note lock
        with open_dict(self.options):
            self.options.update(defaults)
            self.options.update(options)

        # Create expressions
        self.change(a, b, x)

    # Properties
    @property
    def parity(self):
        return "odd"

    @property
    def lead(self):
        return self.a * self.x

    @property
    def const(self):
        return self.b

    @property
    def terms(self):
        return [self.a * self.x, self.b]

    @property
    def coeff(self):
        return [self.a, self.b]

    # Methods
    def derive(self):
        return self.a

    def change(self, a="a", b="b", x="x"):
        """
        Change the terms of the linear polynomial, 
        `a*x + b`, based on the given inputs. Also acts as
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
        # Change terms
        self.a = sympify(a)
        self.b = sympify(b)
        self.x = sympify(x)

        # Change expression
        self.expr = self.a * self.x + self.b

    def factorise(self):
        pass

    # Dunders
    def __str__(self):
        return str(self.expr)
   

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
    line = Linear(a="m", b="c")
    [print(f"{i + 1}. {s}") for i, s in enumerate(dir(line.expr)) if s[0] != "_"]
    breakpoint()