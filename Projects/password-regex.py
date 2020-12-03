# Finds phone numbers and email addresses on the clipboard.

import re
# import pyperclip

passwordRegex = re.compile(r'''(^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$)''')
# password = pyperclip.paste
password = '4554642345Zx@'
result = passwordRegex.fullmatch(password)

if passwordRegex.fullmatch(password):
    print('Password is strong enough')
else:
    print('You suck')
