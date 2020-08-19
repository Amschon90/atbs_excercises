import os, openpyxl
from pathlib import Path

def createHeaders(sheet):
    sheaders = []
    for c in range(1,sheet.max_column+1):
        sheaders.append(sheet.cell(row=1,column=c).value) # Appends the header value to a list
    sheet.delete_rows(1) # Deletes the header row as we don't need it anymore
    return sheaders # All the values in our headers

def createNewSheets(wb,sheet,headers):
    snames = []
    for r in range(1, sheet.max_row+1): # Checks the value in column 1 for the row...
        if sheet.cell(row=r,column=1).value not in snames: # If the value doesn't already have it's own sheet..
            cell = sheet.cell(row=r,column=1).value
            wb.create_sheet(cell) # Create a sheet for it..
            wb[cell].append(headers) # Add our headers to the sheet..
            snames.append(cell) # Add it to the list so we don't have duplicates

def loadDataIntoSheets(sheet, wb):
    for row in sheet.iter_rows(): # For every row in the main sheet..
        newRow = []
        for cell in row: 
            newRow.append(cell.value) # Add all of the values to a list..
        ns = wb[newRow[0]] # Find the sheet matching the first value in the row/list..
        ns.append(newRow) # Add all the values in the row/list to the matching sheet
    wb.remove(sheet) # Remove the main sheet as we don't need it anymore

if __name__ == "__main__":
    # Start program, get the path and the file name
    pathOfFile = Path(input('Please enter your path: '))
    os.chdir(pathOfFile)
    docToSort = input('Please provide the name of the document you wish to be sorted WITHOUT the extension.. ')

    # Open the excel doc
    wb = openpyxl.load_workbook(f'{docToSort}.xlsx')
    sheet = wb.active

    newSheetHeaders = createHeaders(sheet) # Create new sheet headers
    createNewSheets(wb,sheet,newSheetHeaders) # Create new sheets
    loadDataIntoSheets(sheet, wb) # Load the data into sheets
    wb.save(f'sorted{docToSort}.xlsx') # Save the new file