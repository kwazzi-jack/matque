from omegaconf import OmegaConf, open_dict
from omegaconf.dictconfig import DictConfig


class MatqueObject:
    """
    Base object for all `matque` objects to inherit from to
    ensure option parsing and method handling.

    Attributes
    ----------
    options : omegaconf.dictconfig.DictConfig
        contains read-only *class* options for `MatqueObject`, 
        or *class* and *instance* options for instance of `MatqueObject`.
    """
    
    # Default class options, read-only
    options = OmegaConf.create()
    OmegaConf.set_struct(options, True)


    def __init__(self, **options):
        """
        Create instance of `MatqueObject` with copy of class options
        and update with new instance specific options. These options
        are immutable.

        Parameters
        ----------
        options
        """

        # Create new instance options
        instance_options = OmegaConf.create(options)

        # Merge class and instance options
        with open_dict(MatqueObject.options):
            self.options = OmegaConf.merge(
                            MatqueObject.options, instance_options)

        # Set options to read-only
        OmegaConf.set_struct(self.options, True)