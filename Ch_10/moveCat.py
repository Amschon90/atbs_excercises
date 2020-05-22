# Searches a tree and looks for pictures of cats, places them in quarantine..

import shutil, os

sourceFolder = 'C:\\Users\\aschon1\\ATBS Junk Files'            # Identify the folder with the infestation
catFolder = 'C:\\Users\\aschon1\\ATBS Junk Files\\CatPictures'  # Identify the quarantine location

def movePics(folder, catFolder):
    print('Searching for pictures..')
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith('.PNG'):
                ogPath = os.path.join(folder,foldername,filename)
                newPath = os.path.join(catFolder, filename)
                shutil.move(ogPath,newPath)
                print(f'Success!{filename} has been moved to the cat quarantine folder.')

movePics(sourceFolder, catFolder)