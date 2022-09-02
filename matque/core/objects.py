from omegaconf import OmegaConf, open_dict
from omegaconf.dictconfig import DictConfig


class MatqueObject:
    """
    Base object for all `matque` objects to inherit from to
    ensure option parsing and method handling.
    """
    
    def __init__(self) -> None:
        
        # Default class options
        self.options = OmegaConf.create({
            "name" : "MatqueObject"
        })
        
        #OmegaConf.set_struct(self.options, True)