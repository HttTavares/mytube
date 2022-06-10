from vniversvs.space import Space
# from vniversvs.time import Time
from initialization_data import initialization_data
import networkx as nx
from pytube import YouTube
from pytube import Playlist
from vniversvs.mytube import Mytube

class VNIVERSVS(dict):
    """
        Universe is where everything is and happens
    """
    # attrs: []
    def __init__( self, **kwargs ):
        for key in kwargs.keys():
            self[key] = kwargs[key]
        if 'initialization_data' in kwargs.keys():
            for key in kwargs['initialization_data'].keys():
                self[key] = kwargs['initialization_data'][key]
            self.pop("initialization_data", None)
        self.objects = {
            ### PLACE EVERY CLASS HERE LIKE SO:
            # 'class name': class
            'mytube': Mytube,
            'youtube': YouTube,
            'playlist': Playlist,
        }
        # print(self.objects.keys())
        self.space = Space()
        # for object_name in
        # self.downloader = YouTube()
        # self.time = Time()
        for object_name in self.objects.keys():
            self.space[object_name] = {}
        # self.graph = UniversalGraph(
        #     X = nx.DiGraph()
        # )

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__




##########################################################################################
# OBJECT HANDLING #########################################################################################
##########################################################################################

    def create_object( self, object_name, object_initialization_data ):
        object = self.objects[object_name](
            initialization_data = object_initialization_data,
            universe = self
        )
        self.space[object_name][object.name] = object
        # self.collections[f'{object_name}'][object_initialization_data['name']] = object
        self.devs.make_object_metadata(object)
        # self.devs.objectify_object_parameters(object)
        # self.fill_universal_graph( object )
        return object

    def read_object( self, object_id ):
        object = None
        for object_name in self.space.keys():
            if object_id in self.space[collection_name].keys():
                object = self.space[collection_name][object_id]
        return object

    def update_object( self, object_id, new_object_data ):
        try:
            object = self.read_object( object_name )
            for attribute_name in new_object_data.keys():
                try:
                    object.attribute_name = new_object_data[ attribute_name ]
                except:
                    print( 'Could not update attribute', attribute_name )
        except:
            print( 'Could not find object', object_name )

    def delete_object( self, object_name ):
        try:
            for collection_name in self.collections.keys():
                if object_name in self.collections[collection_name].keys():
                    self.collections[collection_name].pop(object_name)
        except:
            print('could not find object', object_name)


##########################################################################################
# ? #########################################################################################
##########################################################################################

    def update( self ):
        # for object_collection in self.collections.values():
        #     for object in object_collection.values():
        #         object.update()
        pass


#
# class VNIVERSVS(dict):
#     """
#         Universe is where everything is and happen
#     """
#     # attrs: []
#     def __init__( self, **kwargs ):
#         for key in kwargs.keys():
#             self[key] = kwargs[key]
#         if 'initialization_data' in kwargs.keys():
#             for key in kwargs['initialization_data'].keys():
#                 self[key] = kwargs['initialization_data'][key]
#             self.pop("initialization_data", None)
#         self.object_collections = {
#         }
#         self.objects = {
#         }
#         for object_name in self.objects.keys():
#             self.collections[f'{object_name}'] = {}
#
#     __getattr__ = dict.__getitem__
#     __setattr__ = dict.__setitem__
#     __delattr__ = dict.__delitem__
#
#     def create_object( self, object_name, object_initialization_data ):
#         self.object_collections[f'{object_name} collection'][object_initialization_data['name']] = self.objects[object_name](
#             initialization_data = object_initialization_data
#         )
#         self.devs.make_object_metadata(
#             self.object_collections[f'{object_name} collection'][object_initialization_data['name']]
#         )
#
#
#
#
# #
