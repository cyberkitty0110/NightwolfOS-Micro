# Userwolf, a username locator developed by cyberkitty0110
#
# FALSE POSITIVES POSSIBLE! PLEASE DO DEEPER RESEARCH AFTER USE!

# Defining Imports
from os import uname
import requests
import time

from nwosimplib import *
# Connecting to an importable function :3
def doxwolf():
    # UNAME INPUT PROMPT
    uname_to_dox = input('[=] Please enter target username: ')

    time.sleep(.5)
    # Main Social Platforms!
    print('SEARCHING MAIN PLATFORMS...PLEASE WAIT.')
    instagram = f'https://www.instagram.com/{uname_to_dox}'
    facebook = f'https://www.facebook.com/{uname_to_dox}'
    twitter = f'https://www.twitter.com/{uname_to_dox}'
    youtube = f'https://www.youtube.com/{uname_to_dox}'
    youtube_alt = f'https://www.youtube.com/c/{uname_to_dox}'

    time.sleep(2)

    print('')
    print('MAIN SEARCH FINISHED, PLEASE WAIT.')

    time.sleep(3)
    clear()

    # Secondary Social Platforms!
    print('SEARCHING SECONDARY PLATFORMS...PLEASE WAIT.')
    google_plus = f'https://plus.google.com/s/{uname_to_dox}'
    reddit = f'https://www.reddit.com/user/{uname_to_dox}'
    github = f'https://www.github.com/{uname_to_dox}'
    tumblr = f'https://www.{uname_to_dox}.tumblr.com'
    pronoun_page = f'https://en.pronouns.page/@{uname_to_dox}'
    carrd = f'https://{uname_to_dox}.carrd.co/'

    # Defining website list!
    WEBSITES = [
        instagram, facebook, twitter, youtube, youtube_alt, google_plus, reddit, github, tumblr, pronoun_page, carrd
    ]

    # Banner!
    def banner():
        ('''
               __                               __ ____
          ____/ /____   _  __ _      __ ____   / // __/
         / __  // __ \ | |/_/| | /| / // __ \ / // /_  
        / /_/ // /_/ /_>  <  | |/ |/ // /_/ // // __/  
        \__,_/ \____//_/|_|  |__/|__/ \____//_//_/                                       
        ''')
    
    # Defining Search!
    def search():

        clear()

        # UNAME INPUT PROMPT
        uname_to_dox = input('[=] Please enter target username: ')

        clear()
        time.sleep(.5)
        # Main Social Platforms!
        print('SEARCHING MAIN PLATFORMS...PLEASE WAIT.')
        instagram = f'https://www.instagram.com/{uname_to_dox}'
        facebook = f'https://www.facebook.com/{uname_to_dox}'
        twitter = f'https://www.twitter.com/{uname_to_dox}'
        youtube = f'https://www.youtube.com/{uname_to_dox}'
        youtube_alt = f'https://www.youtube.com/c/{uname_to_dox}'

        time.sleep(2)

        print('')
        print('MAIN SEARCH FINISHED, PLEASE WAIT.')

        time.sleep(3)
        clear()

        # Secondary Social Platforms!
        print('SEARCHING SECONDARY PLATFORMS...PLEASE WAIT.')
        google_plus = f'https://plus.google.com/s/{uname_to_dox}'
        reddit = f'https://www.reddit.com/user/{uname_to_dox}'
        github = f'https://www.github.com/{uname_to_dox}'
        tumblr = f'https://www.{uname_to_dox}.tumblr.com'
        pronoun_page = f'https://en.pronouns.page/@{uname_to_dox}'
        carrd = f'https://{uname_to_dox}.carrd.co/'

        # Defining website list!
        WEBSITES = [
            instagram, facebook, twitter, youtube, youtube_alt, google_plus, reddit, github, tumblr, pronoun_page, carrd
        ]

        # Banner!
        def banner():
            ('''
                __                               __ ____
            ____/ /____   _  __ _      __ ____   / // __/
            / __  // __ \ | |/_/| | /| / // __ \ / // /_  
            / /_/ // /_/ /_>  <  | |/ |/ // /_/ // // __/  
            \__,_/ \____//_/|_|  |__/|__/ \____//_//_/                                       
            ''')
        
        # Defining Search!
        def search():
            print(f'[=] Searching for username: {uname_to_dox}')
            time.sleep(1)
            print('.')
            time.sleep(.5)
            print('..')
            time.sleep(.5)
            print('...')
            time.sleep(1)

            clear()

            print('doxwolf Is Searching! Please Wait!')
            time.sleep(1)
            print('.')
            time.sleep(.5)
            print('..')
            time.sleep(.5)
            print('...')
            time.sleep(1)

            count = 0
            match = True
            for url in WEBSITES:
                r = requests.get(url)
                if r.status_code == 200:
                    if match == True:
                        print('[!] MATCHES FOUND!')
                        match = False
                    print(f'\n{url} - {r.status_code} - OK')
                    if uname_to_dox in r.text:
                        print(f'POSITIVE MATCH! Username: {uname_to_dox} => Text detected in url.')
                    else:
                        print(f'POSITIVE MATCH! Username: {uname_to_dox} => Text has NOT been detected in url, may be a false positive result.')
                count += 1

            total = len(WEBSITES)
            print(f'SEARCH FINISHED! {count} matches out of {total} sites found!')

            if __name__=='__main__':
                banner()
                search()