import os, openpyxl

PRICE_UPDATES = {'Garlic': 3.07,
                 'Celery': 1.19,
                 'Lemon': 1.27}

os.chdir('C:\\Users\\Zig0n\\Documents\\VSCode Projects\\atbs_excercises\\Ch_13')

wb = openpyxl.load_workbook('produceSales.xlsx')
sheet = wb.active

# Loop over rows
for rowNum in range(2, sheet.max_row):
    produceName = sheet.cell(row=rowNum,column=1).value
    # If row is garlic, celery, or lemons..
    if produceName in PRICE_UPDATES:
        # Change price
        sheet.cell(row=rowNum,column=2).value = PRICE_UPDATES[produceName]
# Save to new file
wb.save('updatedProduceSales.xlsx')
