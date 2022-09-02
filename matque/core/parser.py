import re

def findVars(expr_string : str, vars : list[str]) -> dict:
    pass


def findExpression(
    expr_string : str,
    vars : list[str] = ["x"],
    coeffs : list[str] = ["a"],
    consts : list[str] = ["b"]
) -> dict:
    """
    Parse a expression string and find
    the relevant variables and coefficients that
    are required by the caller.

    Parameters
    ----------
    expr_string : str
        the string representation of the expression to search
        through
    vars : list[str], optional
        symbolic terms to search for in the expression, by default ["x"]
    coeffs : list[str], optional
        the corresponding coefficients to find, by default ["a"]
    consts : list[str], optional
        any constants we would like to find, by default ["a"]

    Returns
    -------
    dict
        dictionary of resulting terms found in expression string
    """

    pass
