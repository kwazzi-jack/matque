import numpy as np
import random as rd
from sympy.core.numbers import Integer, Float
from typing import Tuple, Union
import math
from matque.core import Macros


def seed(n : int = None) -> None:
    """Set the seed for generators that depend
    on randomness. Note, it will overwrite any seed 
    previously being used.

    Args:
        n (int, optional): 
            Integer to set as seed. Default generates 
            its own seed.
    """

    # Choose random time of 32-bit system
    if n == None:
        n = rd.randrange(Macros.MAX_INT)
    
    # Does not like 64-bit time
    rd.seed(n)
    np.random.seed(n)


def integer(
    l: int, 
    u: int
    ) -> Integer:
    """Randomly generate an integer in the given 
    range of `[l, u]` and return as Integer

    Args:
        l (int): 
            Inclusive lowerbound of integer range.
        u (int): 
            Inclusive upperbound of integer range.

    Returns:
        Integer: 
            Sympy version of integer randomly generated.
    """

    return Integer(rd.randint(a=l, b=u))


def decimal(
    l: Union[int, float], 
    u: Union[int, float], 
    r: int=2
    ) -> Float:
    """Randomly generate a float in the given
    range of `[l, u]` and return as Float.

    Args:
        l (Union[int, float]): 
            Inclusive lowerbound of float range.
        u (Union[int, float]): 
            Inclusive upperbound of float range.
        r (int, optional): 
            Number of decimal terms. Default is 2
            decimal places.

    Returns:
        Float:
            Sympy version of float randomly generated.
    """
    num = rd.uniform(l, u)
    return Float(num, r + len(str(int(num))))


def integer_or_decimal(
    l: Union[int, float], 
    u: Union[int, float], 
    r: int=2,
    p: Tuple[float, float]=(0.5, 0.5),
    ) -> Union[Integer, Float]:
    """Randomly generate an integer OR float
    in the given range of `[l, u]` and return
    as resulting type.

    Args:
        l (Union[int, float]): 
            Inclusive lowerbound of integer or float range. 
            If integer, flooring of input is used.
        u (Union[int, float]): 
            Inclusive upperbound of integer or float range.
            If integer, ceiling of input is used.
        r (int, optional): 
            Number of decimal terms. Default is 2
            decimal places.
        p (Tuple[float, float], optional):
            The probabilities to use when choosing either
            integer or decimal, respectively. Default is 
            (0.5, 0.5), i.e., 50/50.

    Returns:
        Union[Integer, Float]: 
            Sympy version of integer or float randomly generated.
    """
    match rd.choices([Macros.INTEGER, Macros.DECIMAL], weights=p)[0]:
        case Macros.INTEGER:
            return integer(math.floor(l), math.ceil(u))
        case Macros.DECIMAL: 
            return decimal(l, u, r)
        case _:
            raise ValueError("Should not be here.")


if __name__ == "__main__":
    l, u = 0, 100
    r = 2
    p = (0.5, 0.5)
    x = integer_or_decimal(l, u, r, p)
    print(x)