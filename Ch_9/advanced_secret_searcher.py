# This tool goes through every file I have specified, searches for a string, and returns a count, the file name,
# and the secrets to you...

import os, re, time

# Open folder, find files
myFiles = os.scandir('C:\\Users\\aschon1\\Documents\\Scripts\\Secret Searcher\\File to Search')

# Set up counters
secretCount = 0
fileCount = 0
lineCount = 0
startTime = time.time()

# Find files
for file in myFiles:
    fileCount += 1
    secretList = []
    print("\nAnalyzing file: %s" % file.name)
    secretFile = open(f'SecretIDs_{os.path.splitext(file.name)[0]}.txt', 'w')
    with open(file) as f:
        for line in f:
            secrets = (re.findall('[0-9]{2}[A-Z][0-9]{9}', line))
            lineCount += 1
            for secret in secrets:
                if secret not in secretList:
                    secretList.append(secret)

    # Print success or failure for user
    if len(secretList) == 0:
        print("There were no secrets found in %s" % file.name)
    else:
        print("There were secrets found in %s. Writing file.." % (file.name))
        for secret in secretList:
            secretFile.write(f"{secret}\n")
        print("File created successfully!")
        secretCount += len(secretList)

    secretFile.close()

# Print performance stats
print("""\n ----- Script run complete! -----
Runtime Stats...
Files Analyzed: %i
Secrets Found: %i
Lines examined: %i
Execution time: %s seconds""" % (fileCount,secretCount,lineCount, time.time() - startTime))