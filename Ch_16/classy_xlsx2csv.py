import csv, openpyxl
from pathlib import Path

#classy_xlsx2csv.py

def convert2csv(xlfile,convDir):
    wb = openpyxl.load_workbook(xlfile)
    for sheet in wb:
        fname=(f'{Path(convDir) / Path(xlfile).stem}_{sheet.title}.csv')
        with open(fname, 'w', newline='') as f:
            print(f'Writing {sheet.title}.csv')
            writer = csv.writer(f)
            writer.writerows([cell.value for cell in row] for row in sheet.rows)

sourceDir = Path(r'C:\Users\Zig0n\Documents\VSCode Projects\xlsx2csv')
convDir = Path(r'C:\Users\Zig0n\Documents\VSCode Projects\xlsx2csv\CONVERTED')

if __name__ == "__main__":
    for file in Path(sourceDir).glob('*.xlsx'):
        print(f'Converting {file.name}...')
        convert2csv(file,convDir)