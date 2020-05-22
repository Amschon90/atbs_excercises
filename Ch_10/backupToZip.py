#! python3
# backupToZip - Copies a folder and makes a zip backup.

import zipfile, os

def backupToZip(folder):
    # Backup folder into zip
    folder = os.path.abspath(folder)

    fileNumber = 1

    while True:
        zipFilename = os.path.basename(folder) + '_' + str(fileNumber) + '.zip'
        if not os.path.exists(zipFilename):
            break
        fileNumber += 1

    # Create the zip file
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename,'w')

    # Walk the entire folder tree and compress folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}')
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue  # don't back up the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')

backupToZip('C:\\Users\\aschon1\\ATBS Junk Files\\Proj_Ch10_JunkDir\\bu')
