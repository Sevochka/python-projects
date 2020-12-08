import shutil, os
from pathlib import Path
import zipfile
import send2trash as send2trash

p = Path.home()

fileSpam = Path.open(p / 'spam.txt', 'w')
fileSpam.write('suck')
fileSpam.close()

    # Path.rmdir(p / 'some-folder')
    # shutil.rmtree(p / 'some-folder')
# send2trash.send2trash('some-folder')
# Path.mkdir(p / 'some-folder')
# To copy a single file
# shutil.copy(p / 'spam.txt', p / 'some-folder')
# shutil.copytree(p, p / 'some-folder2')

# for folderName, subfolders, filenames in os.walk('C:'):
#     print('The current folder is ' + folderName)
#     for subfolder in subfolders:
#         print('SUBFOLDER OF ' + folderName + ': ' + subfolder)
#     for filename in filenames:
#         print('FILE INSIDE ' + folderName + ': '+ filename)
#
#     print('')

# print(p)
# newZip = zipfile.ZipFile(p / 'new.zip', 'w')
# newZip.write(p / 'spam.txt', compress_type=zipfile.ZIP_DEFLATED)
# newZip.close()