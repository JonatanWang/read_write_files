#! python3
# Save & loads pieces of text to the clipboard
# Usage: py.exe updatable_multi_clipboard.pyw save <keyword> - Saves clipboard to keyword.
#       py.exe updatable_multi_clipboard.pyw <keyword> - Loads keyword to clipboard.
#       py.exe updatable_multi_clipboard.pyw list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open("mcb")


# Save clipboard content or delete a keyword from mcb file
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] == pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.pop(sys.argv[2])
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    # Delete all keyword from mcb file
    elif sys.argv[1].lower() == 'delete':
        for k in mcbShelf:
            if k == pyperclip.paste():
                mcbShelf.pop(pyperclip.paste())

mcbShelf.close()