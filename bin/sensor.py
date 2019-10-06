#!/usr/bin/python
import os, requests
from time import sleep
from datetime import datetime
import Adafruit_DHT as DHT

DHT_PIN = int(os.getenv('DHT_PIN'))
DHT_TYPE = getattr(DHT, os.getenv('DHT_TYPE'))
DASHBOARD_HOST = os.getenv('DASHBOARD_HOST')
DASHBOARD_KEY = os.getenv('DASHBOARD_KEY')
SESSION = requests.Session()

while True:
  humidity, temperature = DHT.read_retry(DHT_TYPE, DHT_PIN)
  if humidity is not None and temperature is not None:
    if DASHBOARD_HOST is not None and DASHBOARD_KEY is not None:
      payload = {'func': 'putReading', 'key': DASHBOARD_KEY, 'temperature': temperature, 'humidity': humidity}
      try:
        SESSION.post(DASHBOARD_HOST + '/src/action.php', data=payload, timeout=5.0)
      except requests.exceptions.RequestException as exception:
        print('{0} - {1}'.format(datetime.now(), exception))
    else:
      print('{0} - Dasboard host is not configured'.format(datetime.now()))
      print('Temperature={0:0.2f}*C, Humidity={1:0.2f}%'.format(temperature, humidity))
    sleep(30)
  else:
    print('{0} - Unable to read {1} on GPIO {2}'.format(datetime.now(), DHT_TYPE, DHT_PIN))
    sleep(5)
