#! python3
# mapIt.py - Launches a map in the browser using an address from the command line or clipboard.

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # This means the user entered an address in command line
    address = ' '.join(sys.argv[1:])
else:
    # This means the user wants to use the address from their clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/'+address)