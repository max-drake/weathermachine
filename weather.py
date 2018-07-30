import requests
import json
import datetime
import pprint
import csv

now = datetime.datetime.now()

cities = ['Boston', 'NewYork', 'Chicago', 'LosAngeles']
location = cities[0]

ID = '356ee048e8c81487ca51f04dc70c70a3'
url = 'http://api.openweathermap.org/data/2.5/forecast?q='+location+',us&APPID='+ID

r = requests.get(url).json()
#pprint.pprint(r)

forecast = r['list'] #forecast for next 5 days every 3 hours

next_day_temps=[]

for i in range(8):
	day = forecast[i]
	threehour = day['main']
	temps = threehour['temp']
	next_day_temps.append(temps)


for val in range(len(next_day_temps)):
	next_day_temps[val] = round(1.8 * (next_day_temps[val] - 273) + 32)

hilo_temp = [max(next_day_temps),min(next_day_temps)]

hilo = [hilo_temp]

temp_csv = open('temps.csv','w')
with temp_csv:
	writer = csv.writer(temp_csv)
	writer.writerows(hilo)
