import os, openpyxl

os.chdir('C:\\Users\\Zig0n\\Documents\\VSCode Projects\\atbs_excercises\\Ch_13')

wb = openpyxl.load_workbook('example.xlsx')

print(wb.sheetnames) # The workbook's sheets' names.

sheet3 = wb['Sheet3'] # Get a sheet from the workbook.
print(sheet3)
print(type(sheet3))
print(sheet3.title)

activeSheet = wb.active # Get the active sheet.
print(activeSheet)