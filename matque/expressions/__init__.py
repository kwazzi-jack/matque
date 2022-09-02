from matque.core.objects import MatqueObject
from omegaconf import OmegaConf, open_dict


class Expression(MatqueObject):

    def __init__(self, **options):
        super().__init__()
        
        with open_dict(self.options):        
            self.options.update(options)
        


if __name__ == "__main__":
    x = Expression(name="Expressions", id=12345)
    y = MatqueObject()
    print(x.options)
    print(y.options)