from itertools import count
from omegaconf import OmegaConf, open_dict
from omegaconf.dictconfig import DictConfig
from sympy.core.basic import Basic
from sympy import sympify
from typing import Union
from enum import Enum


# Macros
class Macros(Enum):

    # Errors (0 - 99)
    ERROR = 0

    # Types (100 - 200)
    INTEGER = 100
    DECIMAL = 101
    VARIABLE = 102
    RATIONAL = 103
    IRRATIONAL = 104
    FRACTION = 105
    FUNCTION = 106
    EQUALITY = 107
    INEQUALITY = 108
    GRAPH = 109
    STRING = 110

    # Constants (None)
    MAX_INT = int(2**32 - 1)
    MIN_INT = -MAX_INT


class MatqueObject:
    """
    Base object for all `matque` objects to inherit from to
    ensure option parsing and method handling.
    """

    def __init__(self) -> None:

        # Default class options
        self.options = OmegaConf.create({"class": "MatqueObject"})

        # Lock as struct
        OmegaConf.set_struct(self.options, True)


class Coord:
    def __init__(
        self,
        x: Union[int, float, str, Basic],
        y: Union[int, float, str, Basic],
        label: str = "",
    ):

        if isinstance(x, Basic):
            self.x = x
        else:
            self.x = sympify(x)

        if isinstance(y, Basic):
            self.y = y
        else:
            self.y = sympify(y)

        self.label = label

    def __str__(self) -> str:
        if len(self.label):
            return f"{self.label}({self.x}; {self.y})"
        else:
            return f"({self.x}; {self.y})"

    def __repr__(self) -> str:
        return f"Coord(x={self.x}, y={self.y}, label={self.label})"

    def __setitem__(self, key: int, value: Union[int, float, str, Basic]):
        match key:
            case 0:
                if isinstance(value, Basic):
                    self.x = value
                else:
                    self.x = sympify(value)
            case 1:
                if isinstance(value, Basic):
                    self.y = value
                else:
                    self.y = sympify(value)
            case _:
                raise KeyError()

    def __getitem__(self, key: int):
        match key:
            case 0:
                return self.x
            case 1:
                return self.y
            case _:
                raise KeyError()


if __name__ == "__main__":
    A = Coord(0, sympify("cos(x)") + 1, "A")
    print(A)
    A[1] = sympify("sin(x) - 1")
    print(str(A))
    print(Macros.INTEGER)