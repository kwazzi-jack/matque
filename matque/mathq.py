import numpy as np
import sympy as sp
from abc import ABC, abstractmethod

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

