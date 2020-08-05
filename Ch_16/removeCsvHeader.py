import csv, os

os.chdir('C:\\Users\\Zig0n\\Documents\\VSCode Projects')

# Make a new folder
os.makedirs('headerRemoved',exist_ok=True)

# Loop through all the files in the working folder
for csvFilename in os.listdir('.'):
    if csvFilename.endswith('.csv'):
        print('Removing header from ' + csvFilename + '...')
        
        # Read the CSV file skipping the first row
        csvRows = []
        csvFileObj = open(csvFilename)
        readerObj = csv.reader(csvFileObj)
        for row in readerObj:
            if readerObj.line_num == 1:
                continue
            csvRows.append(row)
        csvFileObj.close()

        # Write all but the header to a CSV file
        csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
        csvWriter = csv.writer(csvFileObj)
        for row in csvRows:
            csvWriter.writerow(row)
        csvFileObj.close()