import pyperclip

# ! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

text = pyperclip.paste()
arr = text.split('\n')
for i, el in enumerate(arr):
    if el.strip() != '':
        arr[i] = '* ' + arr[i].strip()

text = '\n'.join(arr)
pyperclip.copy(text)
