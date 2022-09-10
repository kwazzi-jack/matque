from matque.expressions import Expression


class MatqueError(Exception):
    """
    Custom exception class for matque objects and methods.

    Attributes
    ----------
    error : str
        the identifier of the given exception.
    message : str
        details of the specific `error`.
    remedy : str, optional
        information that can be used to correct this `error`.
    """


    def __init__(self, error : str, message : str, remedy : str):
        """
        Create instance of `MatqueError` with a given error and message,
        with an optional remedy to assist with debug the raised
        issue.

        Parameters
        ----------
        error
        message
        remedy

        See also
        --------
        class `MatqueError`
        """
        
        # Parse attributes
        self.error = error
        self.message = message
        self.remedy = remedy

        # Initialize base class
        super().__init__(message)


    def __str__(self):
        """
        Format string to use when printing contents of error.

        Returns
        -------
        str
            custom error string for given error.
        """

        return f"""
        Error:
            {self.error}
        Details:
            {self.message}
        Remedy:
            {self.remedy}
        """
    

class InvalidOptionError(MatqueError):
    """
    Invalid Option Error class - object with options has been given an option
    that doe not match those of the object.

    Attributes
    ----------
    obj : object
        the object that raised the error.
    option : str
        the mismatched option used in object.
    """


    def __init__(self, obj : object, option : object):
        """
        Create instance of `InvalidOptionError` encompassing option that caused
        the error and the object that raised this error.

        Parameters
        ----------
        obj
        option

        See also
        --------
        class `Error`, class InvalidOptionError
        """

        # Parse attributes
        self.obj = obj
        self.option = option

        # Error parameters for base
        err = "Invalid Option"
        msg = f"`{obj}` has no option `{option}`."
        rem = f"Avaliable options: {list(obj.options.keys())}"

        # Initialize base class
        super().__init__(err, msg, rem)


class OptionValueError(MatqueError):
    """
    Option Value Error class - error raised when invalid value for option of
    specific object is given.

    Attributes
    ----------
    obj : object
        the object that raised the error.
    option : str
        the option used in object.
    value : object
        parsed invalid option value.
    """


    def __init__(self, obj, option, value):
        """
        Create instance of `OptionValueError` encompassing the option that caused
        the error and the object that raised this error.

        Parameters
        ----------
        obj
        option

        See also
        --------
        class `MatqueError`, class `OptionValidError`
        """

        # Parse attributes
        self.obj = obj
        self.option = option
        self.value = value

        # Error parameters for base
        err = "Invalid Option Value"
        msg = f"`{value}` for option `{option}` in "\
                + f"`{obj}` is not valid."
        rem = f"Avaliable choices: {list(obj.options.keys())}"

        # Initialize base class
        super().__init__(err, msg, rem)


class IllegalExpressionError(MatqueError):
    """
    Illegal Expressions class - when a custom expression is given,
    but does not match the general form of the expression itself.

    Attributes
    ----------
    obj : Expression
        the object that raised the error.
    expr : str
        the custom expression that failed.
    gen_expr : str
        correct general expression for object.
    """


    def __init__(self, obj : Expression, expr : str, gen_expr : str):
        """
        Create instance of `IllegalExpressionError` with reference to expression
        object and the custom expression that was invalid.

        Parameters
        ----------
        obj
        expr
        gen_expr

        See also
        --------
        class `MatqueError`, class `IllegalExpressionError`
        """

        # Parse attributes
        self.obj = obj
        self.expr = expr
        self.gen_expr = gen_expr

        # Error parameters for base
        err = "Illegal Expression"
        msg = f"`{expr}` is an illegal form of `{obj.name}`"
        rem = f"{obj.name} has the general form: {gen_expr}"

        # Initialize base class
        super().__init__(err, msg, rem)
