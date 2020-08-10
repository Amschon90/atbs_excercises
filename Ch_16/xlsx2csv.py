# Converts excel docs in a directory to csv files

import os, pathlib, openpyxl, csv

# Identify the source directory
sourceDir = 'C:\\Users\\Zig0n\\Documents\\VSCode Projects\\xlsx2csv'

# Create the new folder path for the converted files
convDir = os.path.join(sourceDir+'\\CONVERTED')
if not os.path.exists(convDir):
    os.makedirs(convDir)

# Identify the source directory and scan it
os.chdir(sourceDir)
myFiles = os.scandir(sourceDir)

# Create a list of all excel files in the source directory
xlsxList = []
for filename in os.listdir('.'):
    if filename.endswith('.xlsx'):
        xlsxList.append(filename)

# Iterate through those files
for exceldoc in xlsxList:
    wb = openpyxl.load_workbook(exceldoc)
    exceldoc = exceldoc.split('.')
    for sheet in wb.sheetnames:
        # Create a new CSV file for each sheet
        outputFile = open(os.path.join(convDir,f'{exceldoc[0]}_{sheet}.csv'),'w',newline='')
        ws = wb[sheet]
        print(f'Writing {exceldoc[0]}_{sheet}.csv is in progress...')
        for r in range(1, ws.max_row + 1):
            # Put each rows data in a list
            rowData = []
            for c in range(1, ws.max_column + 1):
                rowData.append(ws.cell(row=r,column=c).value)
            # ... And then write it to the CSV file
            writer = csv.writer(outputFile)
            writer.writerow(rowData)
        outputFile.close()
        print(f'{exceldoc[0]}_{sheet}.csv has been created!')

print("All files successfully converted!")