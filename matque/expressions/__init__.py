from matque.core.objects import MatqueObject
from matque.core import Macros
from omegaconf import open_dict


class Expression(MatqueObject):
    def __init__(self, **options):

        # Initialize MatqueObject
        super().__init__()

        # Default options
        defaults = {
            "class": "Expression",
            "value": None,
            "mtype": None,
        }

        # Update with new options, note lock
        with open_dict(self.options):
            self.options.update(defaults)
            self.options.update(options)


if __name__ == "__main__":
    x = Expression(name="Expressions", id=12345)
    y = MatqueObject()
    print(x.options)
    print(y.options)
