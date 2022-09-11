import numpy as np
import random


def seed(n : int = None) -> None:
    """Set the seed for generators that depend
    on randomness. Note, it will overwrite any seed 
    previously being used.

    Args:
        n (int, optional): Integer to set as seed. 
            Default generates its own seed.
    """

    # Choose random time of 32-bit system
    if n == None:
        n = random.randrange(int(2**32 - 1))
    
    # Does not like 64-bit time
    random.seed(n)
    np.random.seed(n)


if __name__ == "__main__":
    seed(100)
    print("n:", 100)
    print("Random:", random.random())
    print("Numpy:", np.random.random())

    seed()
    print("n: auto")
    print("Random:", random.random())
    print("Numpy:", np.random.random())