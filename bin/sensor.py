#!/usr/bin/python
import os, requests
from time import sleep
from datetime import datetime
import Adafruit_DHT as DHT

DHT_TYPE = getattr(DHT, os.getenv('SENSOR_TYPE'))
DHT_PIN = os.getenv('SENSOR_PIN')
API_KEY = os.getenv('THINGSPEAK_API_KEY')
TEMP_C = os.getenv('THINGSPEAK_TEMP_C')
TEMP_F = os.getenv('THINGSPEAK_TEMP_F')
HUMIDITY = os.getenv('THINGSPEAK_HUMIDITY')

while True:
  humidity, temperatureC = DHT.read_retry(DHT_TYPE, DHT_PIN)

  if humidity is not None and temperatureC is not None:
    temperatureF = temperatureC * 9 / 5 + 32
    if API_KEY is not None:
      payload = {'api_key': API_KEY, TEMP_C: round(temperatureC, 1), TEMP_F: round(temperatureF, 1), HUMIDITY: round(humidity, 1)}
      r = requests.get('https://api.thingspeak.com/update', params=payload)
      if r.status_code is not requests.codes.ok:
        print('{} - Unable to update thingspeak'.format(datetime.now()))
    else:
      print('{} - THINGSPEAK_API_KEY is empty'.format(datetime.now()))
    sleep(30)
  else:
    print('{} - Unable to read sensor'.format(datetime.now()))
    sleep(5)
