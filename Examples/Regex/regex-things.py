import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')  # Экранирование скобочек
heroRegex = re.compile (r'Batman|Tina Fey') # Batman или Тина

batRegex = re.compile(r'Bat(man|mobile|copter|bat)') # Все что начинается с Bat
batRegex = re.compile(r'Bat(wo)?man') # optional
batRegex = re.compile(r'Bat(wo)*man') # Звездочка - может повтряться сколько угодно раз, даже 0
batRegex = re.compile(r'Bat(wo)+man') # Должно повторяться хотябы 1 раз

haRegex = re.compile(r'(Ha){3}') # 3 раза повтряется

mo = phoneNumRegex.search('My number is 415-555-4242.')
mo.group(1)  # '415'
mo.group(2)  # '555-4242'
mo.group(0)  # '415-555-4242'
mo.group()  # '415-555-4242
areaCode, mainNumber = mo.groups()
