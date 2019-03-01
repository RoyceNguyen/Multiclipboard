#! python3
# mcb.pyw - saves and loads pices of text to the clipboard.
#Usage: py.exe mcb.pyw save <keyword> - saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# TODO: Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print(sys.argv[2] + ' saved successfully')
elif len(sys.argv) == 2:
# TODO: List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys()
                                )))
        print('List of all keywords copied to clipboard')
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        print(sys.argv[1] + ' loaded successfully')

mcbShelf.close()