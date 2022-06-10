class State(dict):
    """
        STATE is a class to handle all the attributes
        of an object, by they builtin data or system objects
        It is used to handle the object itself inside the
        system.

        By convention every object starts with the metadata
        objects DATA, STATE and HISTORY
    """
    def __init__( self, **kwargs ):
        for key in kwargs.keys():
            self[key] = kwargs[key]
        if 'initialization_data' in kwargs.keys():
            for key in kwargs['initialization_data'].keys():
                self[key] = kwargs['initialization_data'][key]
            self.pop("initialization_data", None)
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__
