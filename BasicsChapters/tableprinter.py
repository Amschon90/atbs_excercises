def printTable(table):
    col_widths = [len(max(col, key=len)) for col in table]
    for i in range(4):
        for j in range(3):
            print (table[j][i].rjust(col_widths[j]), end = ' ')
        print('')

tableData = [['apples', 'oranges', 'cherries', 'banana'], ['Alice', 'Bob', 'Carol', 'David'],['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)