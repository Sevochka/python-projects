"""
    Write a program that walks through a folder tree and searches
    for files with a certain file extension (such as .pdf or .jpg).
    Copy these files from whatever location they are in to a new folder.
"""

from pathlib import Path
import os
import shutil

# Массив расширений для переноса
extensions_to_be_selected = ['jpg', 'png']
homePath = Path.home() / 'python-files' / 'selective-copy-project'

copyPath = homePath / 'files-to-copy'
resultPath = homePath / 'result'
# Пересоздать папку result для нового исполнения программы
if Path.is_dir(resultPath):
    shutil.rmtree(resultPath)
Path.mkdir(resultPath)

if not Path.is_dir(copyPath):
    Path.mkdir(copyPath)

for folderName, subfolders, filenames in os.walk(homePath):
    currentFolderPath = Path(folderName)
    for file in filenames:
        try:
            shutil.copy(currentFolderPath / file, resultPath / file)
        except shutil.SameFileError:
            continue
