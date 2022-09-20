# NightwolfOS pentesting microOS, developed by cyberkitty0110

'''Imports'''
from asyncore import read
from genericpath import exists
import time
import os
from os import system, name
import socket


# Defining functions


# Defining the CLEAR function
def clear():

    # For NT-based clients (Windows):
    if name == 'nt':
        _ = system('cls')

    # For UNIX systems (Linux, MacOS, etc. os.name is 'posix')
    else:
        _ = system('clear')

# Hostname and IP address configuration

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

# Kernel and OS loading sequence, purely aesthetic.
#
# Stage One: Locating Kernel
clear()
print('Locating Kernel.')
time.sleep(1)
clear()
print('Locating Kernel..')
time.sleep(1)
clear()
print('Locating Kernel...')
time.sleep(1)
clear()
print('Locating Kernel.')
time.sleep(1)
clear()
print('Locating Kernel..')
time.sleep(1)
clear()
print('Locating Kernel...')
time.sleep(1)
clear()

# Stage Two: Loading OS

print('Kernel found, "NightwolfOS v1.0" now loading.')
time.sleep(0.5)
clear()
print('Kernel found, "NightwolfOS v1.0" now loading..')
time.sleep(0.5)
clear()
print('Kernel found, "NightwolfOS v1.0" now loading...')
time.sleep(0.5)
clear()
print('Kernel found, "NightwolfOS v1.0" now loading.')
time.sleep(0.5)
clear()
print('Kernel found, "NightwolfOS v1.0" now loading..')
time.sleep(0.5)
clear()
print('Kernel found, "NightwolfOS v1.0" now loading...')
time.sleep(0.5)
clear()

# Stage Three: Starting OS

print('Kernel loaded! Starting OS now!')
time.sleep(3)
clear()
print('Your Computer name is: '+hostname)
print('')
print('Your IP address is: '+IPAddr)
time.sleep(.5)
clear()
print('''
    _   __ ( )       __     __                    __ ____   ____  _____
   / | / /__ ____ _ / /_   / /_ _      __ ____   / // __/  / __ \/ ___/
  /  |/ // // __ `// __ \ / __/| | /| / // __ \ / // /_   / / / /\__ \ 
 / /|  // // /_/ // / / // /_  | |/ |/ // /_/ // // __/  / /_/ /___/ / 
/_/ |_//_/ \__, //_/ /_/ \__/  |__/|__/ \____//_//_/     \____//____/  
          /____/                                                                                                                                                                                                       
''')
time.sleep(5)
clear()

# Main Menu

MM = input('''
Welcome to NightwolfOS, {} 

What do you wish to do?
-----------------------
[1] Display System Information
'''.format(hostname))
if MM == 1:
    clear()
