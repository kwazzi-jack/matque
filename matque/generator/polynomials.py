from multiprocessing.sharedctypes import Value
from matque.expressions.polynomials import Linear
from matque import generator as ge
import numpy as np
from typing import Tuple, Union

def create_linear(
    a: Union[int, float, str] = None, 
    b: Union[int, float, str] = None, 
    x: str = "x", 
    l: Union[int, float] = -5, 
    u: Union[int, float] = 5, 
    r: int = 2, 
    p: Tuple[float, float] = (0.5, 0.5),
    coeff_type: str = "int"
    ) -> Linear:

    if a == None and b == None:
        match coeff_type.lower():
            case "i" | "int" | "integer":
                a = ge.integer(l, u)
                b = ge.integer(l, u)
            case "f" | "float" | "decimal":
                a = ge.decimal(l, u, r)
                b = ge.decimal(l, u, r)
            case "m" | "mix" | "mixed":
                a = ge.integer_or_decimal(l, u, r, p)
                b = ge.integer_or_decimal(l, u, r, p)
            case _:
                raise ValueError("Invalid coefficient type.")
    poly = Linear(a, b, x)

    return poly


if __name__ == "__main__":
    line = create_linear()
    print(line)