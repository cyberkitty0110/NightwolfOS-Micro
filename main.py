# NightwolfOS pentesting microOS, developed by NightwolfOffSec

'''Imports'''
from asyncore import read
from genericpath import exists
import time
import os
from os import system, name

def clear():

    # For NT-based clients (Windows):
    if name == 'nt':
        _ = system('cls')

    # For UNIX systems (Linux, MacOS, etc. os.name is 'posix')
    else:
        _ = system('clear')

# --------------------------

print('Locating Kernel...')
time.sleep(1.15)
clear()
print('Kernel found, "NightwolfOS v1.0" now loading...')
time.sleep(1.50)
clear()
print('Kernel loaded! Starting OS now!')
time.sleep(2)
clear()
print('''
d8b   db d888888b  d888b  db   db d888888b db   d8b   db  .d88b.  db      d88888b    .d88b.  .d8888. 
888o  88   `88'   88' Y8b 88   88 `~~88~~' 88   I8I   88 .8P  Y8. 88      88'       .8P  Y8. 88'  YP 
88V8o 88    88    88      88ooo88    88    88   I8I   88 88    88 88      88ooo     88    88 `8bo.   
88 V8o88    88    88  ooo 88~~~88    88    Y8   I8I   88 88    88 88      88~~~     88    88   `Y8b. 
88  V888   .88.   88. ~8~ 88   88    88    `8b d8'8b d8' `8b  d8' 88booo. 88        `8b  d8' db   8D 
VP   V8P Y888888P  Y888P  YP   YP    YP     `8b8' `8d8'   `Y88P'  Y88888P YP         `Y88P'  `8888Y'                                                                                                     
''')
time.sleep(5)
clear()

# --------------------------

Q1 = input('''
What do you wish to do?

[1] Login to current account.
[2] Sign up. (Will replace old accountspace if accountspace exists.)
''')

clear()

if Q1 == '2':
    Password = input('Please enter your password: ')
    while True:
        def doesFileExist(filePathAndName):
            return os.path.exists(filePathAndName)
        if doesFileExist('./Password.txt'):
            with open('Password.txt') as f:
                contents = f.read()
            if contents == Password:
                UserNameS = input('Please enter your new username: ')
                PasswordS = input('Please enter your new password: ')
                with open('Username.txt', 'w' ) as f:
                    f.write(UserNameS)
                with open('Password.txt', 'w') as f:
                    f.write(PasswordS)

                    break
                    clear()
        else:
            with open('Password.txt', 'w') as f:
                f.write(Password)
            print('Password.txt was created. The program will now shutdown.')
            time.sleep(1.10)
            exit()



if Q1 == '1':
    UserName = input("Please enter your username: ")
    Password = input("Please enter your password: ")

    with open('Username.txt') as f:
        contents = f.read()
    with open('Password.txt') as f:
        contents = f.read()

while True:
    if contents == Password:
        print('Login Successful!')
        time.sleep(1)
        clear()
        print('Welcome to NightwolfOS, {}'.format(UserName))
        MainMenu = input('''
                                                                                                   
                What would you like to do today?

                    [1] EXIT OPERATING SYSTEM

                ''')
        break
    else:
        print('Access Denied.')
        print('The program will now shut down.')
        time.sleep(1.15)
        exit()
