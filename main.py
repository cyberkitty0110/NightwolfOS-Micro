# NightwolfOS pentesting microOS, developed by cyberkitty0110
# Defining Libraries
from nwosimplib import *

# Defining functions


# Hostname and IP address configuration

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

# Kernel and OS loading sequence, purely aesthetic.
kernelbootload()
biosstart()
iplog()

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
[1] Exit
'''.format(hostname))
if MainMenu == 1:
    clear()
