from options import Options


class MatqueOptions(Options):
    """
    Base options class for `matque` objects to utilize, with added support
    to ensure correct option parsing.
    """
    pass 


class MatqueObject(object):
    """
    Base object for all `matque` objects to inherit from to
    ensure option parsing and method handling.

    Attributes
    ==========
    options : MatqueOptions
        contains options required by MatqueObject
    name : str
        identifier for `matque` object
    """
    
    # Default class options
    options = MatqueOptions(
                name = "MatqueObject"
            )

    def __init__(self, **kwargs):
        """
        Create instance of `MatqueObject` with given options.

        Parameters
        ----------
        name

        See also
        --------
        class `MatqueObject`, class `MatqueOptions`
        """

        # Parse input options to options
        self.options = MatqueObject.options.push(kwargs)


if __name__ == "__main__":
    options = MatqueOptions()
    print(MatqueObject().options.name)
