'''Imports'''
from asyncore import read
from genericpath import exists
import time
import os
from os import system, name
import socket

# Defining the CLEAR function
def clear():

    # For NT-based clients (Windows):
    if name == 'nt':
        _ = system('cls')

    # For UNIX systems (Linux, MacOS, etc. os.name is 'posix')
    else:
        _ = system('clear')
