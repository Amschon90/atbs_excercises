import os, openpyxl, pprint

os.chdir('C:\\Users\\Zig0n\\Documents\\VSCode Projects\\atbs_excercises\\Ch_13')

# Creating a new doc
wb = openpyxl.Workbook() # Create a blank workbook
sheet = wb.active
sheet.title = '7-14-2020' # Change name
print(sheet.title)

# Changing a sheet name
wb = openpyxl.load_workbook('example.xlsx')
sheet = wb.active
sheet.title = '7-13-2020'

# Creating a sheet
wb.create_sheet(index = 1, title = '07-15-2020')

# Deleting a sheet
del wb['07-15-2020']

# Writing to a sheet
sheet = wb['7-13-2020']
sheet['A1'] = 'Hello, world!'
print(sheet['A1'].value)

# Save everything
wb.save('example_copy.xlsx')