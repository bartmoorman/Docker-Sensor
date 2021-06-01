#!/usr/bin/python3
import os, requests
from time import sleep
from datetime import datetime
import adafruit_dht, board

DASHBOARD_HOST = os.getenv('DASHBOARD_HOST')
DASHBOARD_KEY = os.getenv('DASHBOARD_KEY')
DHT_TYPE = getattr(adafruit_dht, os.getenv('DHT_TYPE', 'DHT22'))
DHT_PIN = getattr(board, os.getenv('DHT_PIN', 'D17'))
FREQUENCY = os.getenv('FREQUENCY', 30)
SESSION = requests.Session()
SENSOR = DHT_TYPE(DHT_PIN)

print('''Starting Sensor with the following settings:
DASHBOARD_HOST: {0}
DASHBOARD_KEY: {1}
DHT_TYPE: {2}
DHT_PIN: {3}
FREQUENCY: {4}
'''.format(DASHBOARD_HOST or '[unset]', '[redacted]' if DASHBOARD_KEY else '[unset]', DHT_TYPE.__name__, DHT_PIN or '[unset]', FREQUENCY))

if DASHBOARD_HOST is not None and DASHBOARD_KEY is not None:
  DASHBOARD = True
else:
  print('{0} - Dashboard is not configured. Readings will be sent to stdout.'.format(datetime.now()))
  DASHBOARD = False

while True:
  try:
    temperature = SENSOR.temperature
    humidity = SENSOR.humidity

    if DASHBOARD:
      payload = {'func': 'putReading', 'key': DASHBOARD_KEY, 'temperature': temperature, 'humidity': humidity}

      try:
        SESSION.post(DASHBOARD_HOST + '/src/action.php', data=payload, timeout=5.0)
      except requests.exceptions.RequestException as exception:
        print('{0} - {1}'.format(datetime.now(), exception))
    else:
      print('{0} - Temperature={1:0.2f}°C, Humidity={2:0.2f}%'.format(datetime.now(), temperature, humidity))

    sleep(int(FREQUENCY))
  except RuntimeError as exception:
      print('{0} - Unable to read {1} on GPIO {2} ({3})'.format(datetime.now(), DHT_TYPE.__name__, DHT_PIN, exception))
      sleep(2)
