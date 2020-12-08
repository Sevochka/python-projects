from pathlib import Path
import os

p = Path('D:\\Data\\Desktop\\spam.txt')
# print(p)
# p.write_text('hello world')

# p.read_text()
fileTxt = p.open('a')

fileTxt.write('23145')
fileTxt.close()