class Data(dict):
    """
        DATA is a class to handle the basic data
        (builtin data) of an object. It is also
        used to generate the data to analyze the
        behavior of the system after its releases

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



#
