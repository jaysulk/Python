# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:08:48 2017

@author: jsulskis

Get historic meteorological conditions for MODTRAN selection in DSM.

Note: Free API key is limited to 500 calls per day/10 calls per minute!

"""

from urllib.request import urlopen
from datetime import date as dt
import json

# Input parameters for search
year = input("Enter year:")
month = input("Enter month:")
day = input("Enter day:")
hour = input("Enter hour (local time/24 hr format):")
latlong = input("Enter Lat,Long:")
latlong = latlong.replace(" ", "")

# Convert date to api URL format
date = dt(int(year), int(month), int(day))
date = date.strftime("%Y%m%d")

# Get historic meteorological conditions from Wunderground API
key = 'xxxxxxxxxxxxxxxx' # Limited to 500 calls per day/10 calls per minute
url = 'http://api.wunderground.com/api/'+key+'/history_'+date+'/q/'+latlong+'.json'
f = urlopen(url)
json_string = f.read().decode('utf8')
parsed_json = json.loads(json_string)
data = parsed_json['history']['observations']
hour = '{:02}'.format(int(hour))
result = next(item for item in data if item["date"]["hour"] == hour)
temp = result['tempm']
dewp = result['dewptm']
tempf = result['tempi']
press = result['pressurem']
hum = result['hum']
windir = result['wdire']
winspd = str(float(result['wspdi'])*0.868976242)


# Print results
print("\n")
print("Station ID: "+result['metar'][6:10])
print("Temperature (\N{DEGREE SIGN}C) = "+temp+"\N{DEGREE SIGN}")
print("Temperature (\N{DEGREE SIGN}F) = "+tempf+"\N{DEGREE SIGN}")
print("Dew Point (\N{DEGREE SIGN}C) = "+dewp+"\N{DEGREE SIGN}")
print("Relative Humidity = "+hum+"%")
print("Barometric Pressure = "+press+" mbar")
print("Wind Speed = "+winspd+" kts")
print("Wind Direction = "+windir)

# Close JSON file
f.close()

