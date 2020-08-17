# Downloads Cyanide & Happiness, daily.

import bs4, requests, datetime, os, glob
from pathlib import Path

def checkForNewComic(url,dir):
    res = requests.get(url)
    res.raise_for_status()
    comicSoup = bs4.BeautifulSoup(res.text,'html.parser')
    if getWebDate(comicSoup) > getFileDate(dir):
        downloadComic(comicSoup, dir)
    else:
        print('The latest comic has already been downloaded.')
        
def getWebDate(webpage):
    comicDate = str(webpage.find('div',id='comic-author').text)[1:11]
    comicDate = datetime.datetime.strptime(comicDate, '%Y.%m.%d')
    return comicDate
    
def getFileDate(dir):
    list_of_paths = dir.glob('*')
    latest_File = Path(max(list_of_paths, key=os.path.getctime)).stem
    fileDate = datetime.datetime.strptime(latest_File, '%Y.%m.%d')
    return fileDate

def downloadComic(webpage, dir):
    comicUrl = webpage.find('img',id='main-comic').get('src')
    fileName = str(webpage.find('div',id='comic-author').text)[1:11]
    res = requests.get('https:' + comicUrl)
    res.raise_for_status()
    comicImg = open(f'{fileName}.png','wb')
    for chunk in res.iter_content(100000):
        comicImg.write(chunk)
    comicImg.close()

if __name__ == '__main__':
    comicDir = Path(r'C:\Users\Zig0n\Documents\Cyanide&Happiness')
    os.chdir(comicDir)
    checkForNewComic('http://explosm.net/',comicDir)