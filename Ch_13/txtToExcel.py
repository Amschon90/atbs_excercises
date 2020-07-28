import os, openpyxl

# Set working directory
os.chdir('C:\\Users\\Zig0n\\Documents\\VSCode Projects\\atbs_excercises\\Ch_13')
# Scan my documents folder for files
myFiles = os.scandir('C:\\Users\\Zig0n\\Documents\\txt_files_atbs')

# Set up list
allList = []

for file in myFiles:
    with open(file) as f:
        alist = [line.rstrip() for line in f] # Scan files, insert each line as a new row
        alist.insert(0,file.name.rsplit('.',1)[0].upper()) # Insert the file name to the front of the list
        allList.append(alist) # Append list to main list

# Open Excel, create new file
wb = openpyxl.Workbook()
sheet = wb.active

# Create a column for each list within allList, add each item to the rows
for c in range(len(allList)):
    for r in range(len(allList[c])):
        sheet.cell(row=r+1,column=c+1).value = allList[c][r]

# Save
wb.save('myFilesToExcel.xlsx')
print('Completed successfully!')