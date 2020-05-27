# Script to find giant files in my documents

import shutil, os

folder = ('C:\\Users\\aschon1\\Documents')

def fileSizeSearch(folder):
    potentialfreedmemory = 0
    filecounter = 0
    print('Searching for pictures..')
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            filesize = os.path.getsize(os.path.join(folder, foldername, filename))
            if filesize >= 100000000:
                potentialfreedmemory += filesize
                filecounter += 1
                print(f'{filename} has a size of {int(filesize/1000000)}MB and should be deleted or archived.')
    print(f"By deleting these {filecounter} files, you could free up {int(filesize/1000000)}MB of memory.")

fileSizeSearch(folder)