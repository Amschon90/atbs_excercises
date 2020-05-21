# This tool goes through every file I have specified, searches for a string, and returns a count, the file name,
# and the secrets to you...

import os, re

# Open folder, find files
myFiles = os.scandir('C:\\Users\\aschon1\\Documents\\Project Files ATBS')
secretFile = open(f'SecretIDs.txt', 'w')

# Find files
for file in myFiles:
    # Open a file
    fileOpen = open(file)
    secretFile = open(f'SecretIDs_.txt', 'w')

    # Read it and assign it to a variable, then close file
    fileRead = fileOpen.read()
    fileOpen.close()

    # Find all instances of my secret in the file
    secrets = (re.search('[0-9]{2}[A-Z][0-9]{9}', fileRead))

    # Print the file name and count of secrets, then print each secret on it's own line.
    if len(secrets) == 0:
        print("\nThere were no secrets found in %s" % file.name)
    else:
        print("\nThere were %i secrets found in %s. Writing file.." % (len(secrets), file.name))
        for secret in secrets:
            secretFile.write(f"{secret}\n")
        print("File created successfully! End of script.")

    secretFile.close()
