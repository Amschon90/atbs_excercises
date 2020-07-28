import os, openpyxl

# Set working directory
os.chdir('C:\\Users\\Zig0n\\Documents\\VSCode Projects\\atbs_excercises\\Ch_13')
# Scan my documents folder for files
mainPath = ('C:\\Users\\Zig0n\\Documents\\txt_files_atbs')

# Set up list
allList = []

# Open excel, read the file, create allList again
wb = openpyxl.load_workbook('myFilesToExcel.xlsx')
sheet = wb.active

for c in range(1,sheet.max_column+1):
    # Create a working dictionary..
    wlist = []
    for r in range(1,sheet.max_row+1):
        # Add the value to the working dictionary..
        wlist.append(sheet.cell(row=r,column=c).value)
        # Then clear the cell..
        sheet.cell(row=r,column=c).value = ''
    # Add the working dictionary to the items dictionary
    allList.append(wlist)

for i in range(len(allList)):
    fileName = allList[i].pop(0)
    txtFile = open(os.path.join(mainPath,f'{fileName.lower()}.txt'), 'w')
    txtFile.writelines("%s\n" % l for l in allList[i])
    txtFile.close()
    
print('Success!')