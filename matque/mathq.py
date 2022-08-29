import numpy as np
import sympy as sp
from abc import ABC, abstractmethod


class Error(Exception):

    def __init__(self, code, message, remedy):
        self.code = code
        self.message = message
        self.remedy = remedy
        super().__init__(message)


    def __str__(self):
        return f"""
        Error-code:
            {self.code}
        Details:
            {self.message}
        Remedy:
            {self.remedy}
        """


class InvalidOptionError(Error):

    def __init__(self, obj, option):
        self.obj = obj
        self.option = option
        self.code = "Invalid Option"
        self.message = f"`{obj}` has no option `{option}`"
        self.remedy = f"Avaliable options: {list(obj.options.keys())}"
        super().__init__(self.code, self.message, self.remedy)


class OptionValueError(Error):

    def __init__(self, obj, option, value, correct_values):
        self.obj = obj
        self.option = option
        self.value = value
        self.code = "Invalid Option Value"
        self.message = f"`{value}` for option `{option}` in `{obj}` is not valid."
        self.remedy = f"Avaliable choices: {list(obj.options[option])}"
        super().__init__(self.code, self.message, self.remedy)


class MathqObject(object):

    def __init__(self):
        pass

    
    def _process_options(self, options):
        
        
        for option, value in options.items():
            try:
                if value not in self.options[option]:
                    raise OptionValueError(self, option,
                            value, self.options[option])
                else:
                    setattr(self, option, value)
            except KeyError:
                raise InvalidOptionError(self, option)


class Expression(MathqObject):
    
    def __init__(self):
        pass



class Polynomial(Expression):

    def __init__(self):
        pass        


class Linear(Polynomial):
    
    # Linear Class Specific Options
    options = {
            "etype":
                ["polynomial", "line"]
            }
   

    def __init__(self, **options):
        super().__init__()
        self._process_options(options)
        

class Quadratic(Polynomial):

    def __init__(self):
        super().__init__()

if __name__ == "__main__":
    eq = Linear(hello=2)

