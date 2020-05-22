#! python3
# backupToZip - Copies a folder and makes a zip backup.

import zipfile, os

def backupToZip(folder):
    # Backup folder into zip
    folder = os.path.abspath(folder)

    fileNumber = 1

    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        fileNumber += 1

    # TODO: Create the zip file

    # TODO: Walk the entire folder tree and compress folder.

    print('Done.')


backupToZip('C:\\Users\\aschon1\\ATBS Junk Files\\Proj_Ch10_JunkDir\\bu')
