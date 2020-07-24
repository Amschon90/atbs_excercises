# Takes 3 arguments, and then inserts blank rows where you tell it to.
# Ex., python blankRowInserter.py 3 2 myss.xlxs will insert 2 blank rows @ row 3

import os, openpyxl, sys

os.chdir('C:\\Users\\Zig0n\\Documents\\VSCode Projects\\atbs_excercises\\Ch_13')

# Open the spreadsheet
wb = openpyxl.load_workbook(sys.argv[3])
sheet = wb.active

# Insert the blank rows
sheet.insert_rows(int(sys.argv[1]),amount=int(sys.argv[2]))

# Save the new spreadsheet
wb.save(f'BRI_{sys.argv[3]}')