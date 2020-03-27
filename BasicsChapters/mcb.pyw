# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw delete <keyword> - Deletes specified keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#        py.exe mcb.pyw delete - Deletes all keywords in the shelf.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete':
        for keywords in list(mcbShelf.keys()):
            del mcbShelf[keywords]

mcbShelf.close()
