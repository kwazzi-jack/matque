import numpy as np
import random
from sympy import Integer, Float


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
        n = random.randrange(int(2**32 - 1))
    
    # Does not like 64-bit time
    random.seed(n)
    np.random.seed(n)


def integer(l: int, u: int) -> Integer:
    """Randomly generate an integer in the given 
    range of `[l, u]` and return Integer

    Args:
        l (int): 
            Inclusive lowerbound of integer range.
        u (int): 
            Inclusive upperbound of integer range.

    Returns:
        Integer: 
            Sympy version of integer randomly generated.
    """

    return Integer(random.randint(a=l, b=u))


def decimal(l: int, u: int, r: int=2) -> Float:
    """Randomly generate a float in the given
    range of `[l, ]

    Args:
        l (int): _description_
        u (int): _description_
        r (int, optional): _description_. Defaults to 2.

    Returns:
        Float: _description_
    """
    num = random.uniform(l, u)
    return Float(num, r + len(str(int(num))))


if __name__ == "__main__":
    l, u = 0, 100
    x1 = integer(l, u)
    print(x1)

    x2 = decimal(l, u)
    print(x2)