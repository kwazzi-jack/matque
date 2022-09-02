from matque.expressions import Expression


class Polynomial(Expression):
    """
    General polynomial object
    """
    pass


class Linear(Polynomial):
    """
    Polynomial of degree=1
    """
    pass


class NumericLinear(Linear):
    """
    Linear polynomial with assigned values
    """


class Quadratic(Polynomial):
    """
    Polynomial of degree=2
    """
    pass


class NumericQuadratic(Quadratic):
    """
    Quadractic polynomial with assigned values
    """


class Cubic(Polynomial):
    """
    Polynomial of degree=2
    """
    pass


class NumericCubic(Cubic):
    """
    Cubic polynomial with assigned values
    """