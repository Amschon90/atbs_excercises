import os, openpyxl

os.chdir('C:\\Users\\Zig0n\\Documents\\VSCode Projects\\atbs_excercises\\Ch_13')

# Load workbook
wb = openpyxl.load_workbook('produceSold.xlsx')
sheet = wb.active

# Items dictionary
items = []

# Go through each row and column..
for c in range(1,sheet.max_column+1):
    # Create a working dictionary..
    wdict = []
    for r in range(1,sheet.max_row+1):
        # Add the value to the working dictionary..
        wdict.append(sheet.cell(row=r,column=c).value)
        # Then clear the cell..
        sheet.cell(row=r,column=c).value = ''
    # Add the working dictionary to the items dictionary
    items.append(wdict)

# Create the inverted excel doc..
for ic in range(len(items)):
    for ir in range(len(items[ic])):
        sheet.cell(row=ic+1,column=ir+1).value = items[ic][ir]

wb.save('invertedproduceSold.xlsx')

print('Done!')