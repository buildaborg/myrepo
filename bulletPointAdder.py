#! python 3
# bulletPointAdder.py - Adds Wikipedia points to the start
# of each line of test on the clipboard.

import pyperclip
text = pyperclip.paste()

# TODO: Separate lines and add stars.
#Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)): # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines"list
    
text = '\n'.join(lines)

pyperclip.copy(text)

