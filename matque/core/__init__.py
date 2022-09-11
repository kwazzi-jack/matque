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