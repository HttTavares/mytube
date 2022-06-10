from devs import DEVS
from moviepy.editor import *
import os
from natsort import natsorted
# from vniversvs import VNIVERSVS

devs = DEVS()
devs.fiat()
universe = devs.universe
tester = devs.tester
cli = devs.cli
autogit = devs.autogit

# if devs.window_flag:
#     import pygame
#     from PyQt5 import QtCore, QtGui, QtWidgets
#     window = devs.window


def main():

    ### Automate Git System
    ###
    ###

    # test1

    print(autogit.repo)
    devs.env = input('what env? ')
    devs.run_cli()

    pass

if __name__ == '__main__':
    main()
