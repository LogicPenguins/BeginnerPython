#! python3
# open_weather.py - Prints the weather for a location from the command line.

import json, requests, sys

APP_ID = 'Insert_ID_Here'


# Computer location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: open_weather.py city_name, 2-letter_country_code')
    sys.exit()

location = ' '.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url = f'https://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=3&APPID=%s ' % (location, APP_ID)

response = requests.get(url)
response.raise_for_status()

print(response.text)
