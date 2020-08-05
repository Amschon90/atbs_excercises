import os,csv

os.chdir('C:\\Users\\Zig0n\\Documents\\VSCode Projects\\atbs_excercises\\Ch_16')

exampleFile = open('exampleWithHeader.csv')
exampleDictReader = csv.DictReader(exampleFile)

for row in exampleDictReader:
    print(row['Timestamp'],row['Fruit'],row['Quantity'])