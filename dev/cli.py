from initialization_data import initialization_data
import json
import pandas as pd

class CLI(dict):
    """
        CLI is a basic user interface to use the app
    """
    def __init__( self, **kwargs ):
        for key in kwargs.keys():
            self[key] = kwargs[key]
        if 'initialization_data' in kwargs.keys():
            for key in kwargs['initialization_data'].keys():
                self[key] = kwargs['initialization_data'][key]
            self.pop("initialization_data", None)
        self.commands = {}

    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

    def flag_selected( self ):
        if 'selected' in self.keys():
            return True
        else:
            return False

    def execute_command( self, command_text ):
        if self.devs.env == 'p':
            try:
                self.commands[command_text]()
            except:
                print('no such command, brah')
        if self.devs.env == 'd':
            self.commands[command_text]()
        print()

    def get_parameter_list( self, parameter ):
        list1 = parameter.split(',')

    def parse_commands( self, command_text ):
        parameter_list = command_text.split(' @ ')
        ret = {}
        for parameter in parameter_list[1:]:
            if ' = ' in parameter:
                pair = parameter.split(' = ')
                ret[pair[0]] = pair[1]
        self.current_command = parameter_list[0]
        self.current_parameters = ret
        return ret

    def command_q( self ):
        # self.command_save()
        print('hello')
        quit()
        # print('goodbye')

    def command_test( self ):
        tester = self.devs.tester
        # print(tester.tests[self.current_parameters['name']])
        # print(self.selected)
        tester.tests[self.current_parameters['name']](self.selected)

    def command_select( self ):
        # self.selectable = self.universe.collections['project'].keys()
        self.selectable = []
        if self.current_parameters['name'] in self.selectable:
            self.selected = self.current_parameters['name']
            print('you have selected:', self.selected)
        else:
            print('could not find object', self.current_parameters['name'])
            print('did you mean: ')
            for selectable_name in self.selectable:
                print(selectable_name)

    def command_download( self ):
        # print(self.current_parameters)
        self.universe.mytube = self.universe.create_object(
            'mytube',
            object_initialization_data = self.current_parameters
        )
        # print(self.universe.mytube.link)
        self.universe.mytube.download()

    def command_save( self ):
        pass

    def command_load( self ):
        pass
