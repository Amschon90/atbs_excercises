import os, openpyxl

os.chdir('C:\\Users\\Zig0n\\Documents\\VSCode Projects\\atbs_excercises\\Ch_13')

wb = openpyxl.load_workbook('example.xlsx')

sheet = wb['Sheet1'] # Get a sheet from the workbook.
print(sheet['A1']) # Get a cell from the sheet.
print(sheet['A1'].value) # Get the value from the cell.

# Get another cell from the sheet.
c = sheet['B1']
print(c.value)

# Get the row, column, and value from the cell.
print('Row %s, Column %s is %s' % (c.row, c.column, c.value))
print('Cell %s is %s' % (c.coordinate, c.value))
print(sheet['C1'].value)

# Get coordinates then value
print(sheet.cell(row=1, column=2))
print(sheet.cell(row=1, column=2).value)

for i in range(1,8,2): # Print every other row
    print(i, sheet.cell(row=i, column=2).value)

# Getting max row & column number
print(sheet.max_row)
print(sheet.max_column)
