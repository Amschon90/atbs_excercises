import bs4, requests

# Working from a page..
#res = requests.get('https://forecast.weather.gov/MapClick.php?lat=40.99668211159686&lon=-80.68342626918752#.XtgMWDpKhPY')
#res.raise_for_status()
#weatherSoup = bs4.BeautifulSoup(res.text,'html.parser')
#weather = weatherSoup.select('detailed-forecast-body > div:nth-child(2) > div.col-sm-10.forecast-text')
#print(weather) # An example using inspect element > CSS Copy

# Working with a file..
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile,'html.parser')

# Will match any element that has an id attribute of author, as long as it is also inside a <p> element
elems = exampleSoup.select('p #author')
print(type(elems)) # elems is a list of tag objects
print(len(elems))
print(type(elems[0]))
print(str(elems[0]))
print(elems[0].getText())
print(elems[0].attrs)