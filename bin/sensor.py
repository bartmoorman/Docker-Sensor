#!/usr/bin/python
import os, requests
from time import sleep
from datetime import datetime
import Adafruit_DHT as DHT

DHT_PIN = os.getenv('DHT_PIN')
DHT_TYPE = getattr(DHT, os.getenv('DHT_TYPE', 'DHT22'))
DASHBOARD_HOST = os.getenv('DASHBOARD_HOST')
DASHBOARD_KEY = os.getenv('DASHBOARD_KEY')
FREQUENCY = os.getenv('FREQUENCY', 30)
SESSION = requests.Session()

print '''Starting Sensor with the following settings:
DHT_PIN: {0}
DHT_TYPE: {1}
DASHBOARD_HOST: {2}
DASHBOARD_KEY: {3}
FREQUENCY: {4}
'''.format(DHT_PIN or '[unset]', DHT_TYPE, DASHBOARD_HOST or '[unset]', '[set]' if DASHBOARD_KEY else '[unset]', FREQUENCY)

if DASHBOARD_HOST is None or DASHBOARD_KEY is None:
  print('Dashboard is not configured. Readings will be sent to stdout.')

while True:
  if DHT_PIN is not None:
    humidity, temperature = DHT.read_retry(DHT_TYPE, int(DHT_PIN))
    if humidity is not None and temperature is not None:
      if DASHBOARD_HOST is not None and DASHBOARD_KEY is not None:
        payload = {'func': 'putReading', 'key': DASHBOARD_KEY, 'temperature': temperature, 'humidity': humidity}
        try:
          SESSION.post(DASHBOARD_HOST + '/src/action.php', data=payload, timeout=5.0)
        except requests.exceptions.RequestException as exception:
          print('{0} - {1}'.format(datetime.now(), exception))
      else:
        print('{0} - Temperature={1:0.2f}*C, Humidity={2:0.2f}%'.format(datetime.now(), temperature, humidity))
      sleep(FREQUENCY)
    else:
      print('{0} - Unable to read {1} on GPIO {2}'.format(datetime.now(), DHT_TYPE, DHT_PIN))
      sleep(5)
  else:
    print('DHT_PIN is required.')
    sleep(60)
