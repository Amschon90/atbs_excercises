import os, census2010

anchoragePop = census2010.allData['OH']['Mahoning']['pop']
print('The 2010 population of Mahoning County was ' + str(anchoragePop))