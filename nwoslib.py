import time
import os
import socket
import psutil

from os import system, name
from asyncore import read
from genericpath import exists
from startup import kernelbootload, biosstart, iplog, clear
