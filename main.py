# NightwolfOS pentesting microOS, developed by cyberkitty0110

# Defining Libraries
from nwosimplib import *

# Defining functions
def startup():
    kernelbootload()
    biosstart()
    iplog()

# Hostname and IP address configuration

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

# Startup sequence, purely aesthetic.
startup()

clear()
print('''
    _   __ ( )       __     __                    __ ____   ____  _____
   / | / /__ ____ _ / /_   / /_ _   _  __ ____   / // __/  / __ \/ ___/
  /  |/ // // __ `// __ \ / __/| | /| / // __ \ / // /_   / / / /\__ \ 
 / /|  // // /_/ // / / // /_  | |/ |/ // /_/ // // __/  / /_/ /___/ / 
/_/ |_//_/ \__, //_/ /_/ \__/  |__/|__/ \____//_//_/     \____//____/  
          /____/                                                                                                                                                                                                       
''')
time.sleep(5)
clear()

# Main Menu

MainMenu = input('''
Welcome to NightwolfOS, {} 

What do you wish to do?
-----------------------
[1] doxwolf (Username DOXXER)

'''.format(hostname))
if MainMenu == '1':
    doxwolf.doxwolf()
else:
    exit
    
