import json, requests

location = input('Enter a US city: ')
APPID = 'b7804c5eed6363309519c0ac4d5538e2'
url ='http://api.openweathermap.org/data/2.5/weather?q=%s,us&APPID=%s&units=imperial' % (location,APPID)

response = requests.get(url)
response.raise_for_status()

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData['main']
print('Current weather in %s:' % (location))
print('Currently it is %i degrees, with %i percent humidity.' % (w['temp'],w['humidity']))