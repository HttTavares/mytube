from dev.tester import Tester
from vniversvs.vniversvs import VNIVERSVS
from dev.cli import CLI
from dev.state import State
from dev.data import Data
from dev.autogit import AutoGit
from dev.arcanum import Arcanum
# from git import Repo
import git

from initialization_data import initialization_data


class DEVS(dict):
    """
        Universe is where everything is and happen
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

    def make_object_metadata( self, object ):
        object.state = State()
        # object.history = History()
        object.data = Data()
        object.universe = self.universe
        object.devs = self

    def fiat( self ):
        self.fiat_universe()
        self.fiat_arcanum()
        self.fiat_tester()
        self.fiat_cli()
        self.fiat_autogit()

    def fiat_universe( self ):
        self.universe = VNIVERSVS(
            initialization_data = initialization_data['universe']
        )
        self.make_object_metadata( self.universe )
        return self.universe
        print('universe created')

    def fiat_tester( self ):
        self.tester = Tester()
        self.tester.universe = self.universe
        self.tester.devs = self
        print('tester created')

    def fiat_cli( self ):
        self.cli = CLI()
        self.cli.universe = self.universe
        self.cli.devs = self
        self.fiat_commands()
        print('cli created')

    def run_cli( self ):
        self.cli.next_command = ''
        while self.cli.next_command != 'q':
            self.cli.next_command = input("type a command: ")
            self.cli.parsed_command = self.cli.parse_commands( self.cli.next_command )
            self.cli.execute_command( self.cli.current_command )
            self.universe.update()
        print('bye bye')

    def fiat_commands( self ):
        with open('dev/cli.py') as tmp:
            tmp = tmp.read().split('\n')
            for line in tmp:
                if 'def command_' in line and '#' not in line:
                    command_name = line[8:]
                    command_name = command_name.split('(')[0]
                    command_key = command_name[8:]
                    # print('command_name', command_name)
                    self.cli.commands[command_key] = getattr(self.cli, command_name)

    def fiat_autogit( self ):
        self.autogit = AutoGit()
        self.autogit.repo = git.Repo.clone_from(
            self.arcanum.remote_url,
            self.arcanum.local_folder
        )
        self.make_object_metadata( self.autogit )
        print('autogit created')

    def fiat_arcanum( self ):
        self.arcanum = Arcanum()
        self.make_object_metadata( self.arcanum )
        print('arcanum created')



#
