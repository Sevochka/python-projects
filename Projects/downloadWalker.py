"""
    Write a program that walks through a folder tree and searches
    for exceptionally large files or folders—say,
    ones that have a file size of more than 100MB.
    (Remember that to get a file’s size, you can use
    os.path.getsize() from the os module.)
    Print these files with their absolute path to the screen.
"""
import os
from pathlib import Path

resultArr = []
# Расположение папки "Загрузки" на моем компьютере
downloadFolder = Path('D:/Data/Downloads')

if not Path.is_dir(downloadFolder):
    downloadFolder = Path.home() / 'Downloads'

for folderName, subFolders, fileNames in os.walk(downloadFolder):
    folderPath = Path(folderName)
    for file in fileNames:
        currentPath = folderPath / file
        size = os.path.getsize(Path(folderName) / file)
        if size >= 100000:
            resultArr.append({'path': str(currentPath), 'size': size})

print(resultArr)

