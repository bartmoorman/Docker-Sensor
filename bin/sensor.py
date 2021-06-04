#!/usr/bin/python3
import os, requests
from time import sleep
from datetime import datetime
import pigpio_dht

DASHBOARD_HOST = os.getenv('DASHBOARD_HOST')
DASHBOARD_KEY = os.getenv('DASHBOARD_KEY')
SENSOR_TYPE = getattr(pigpio_dht, os.getenv('SENSOR_TYPE', 'DHT22'))
SENSOR_PIN = os.getenv('SENSOR_PIN', 17)
SENSOR_SAMPLES = os.getenv('SENSOR_SAMPLES', 5)
SENSOR_FREQUENCY = os.getenv('SENSOR_FREQUENCY', 5)
SENSOR_TIMEOUT = os.getenv('SENSOR_TIMEOUT', 0.5)

print('''Starting Sensor with the following settings:
DASHBOARD_HOST: {0}
DASHBOARD_KEY: {1}
SENSOR_TYPE: {2}
SENSOR_PIN: {3}
SENSOR_SAMPLES: {4}
SENSOR_FREQUENCY: {5}
SENSOR_TIMEOUT: {6}
'''.format(DASHBOARD_HOST or '[unset]', '[redacted]' if DASHBOARD_KEY else '[unset]', SENSOR_TYPE, SENSOR_PIN or '[unset]', SENSOR_SAMPLES, SENSOR_FREQUENCY, SENSOR_TIMEOUT))

if DASHBOARD_HOST is not None and DASHBOARD_KEY is not None:
  DASHBOARD = True
else:
  print('{0} - Dashboard is not configured. Readings will be sent to stdout.'.format(datetime.now()))
  DASHBOARD = False

print('{0} - Setting up sensor'.format(datetime.now()))
SENSOR = SENSOR_TYPE(int(SENSOR_PIN), timeout_secs=float(SENSOR_TIMEOUT))

print('{0} - Setting up session'.format(datetime.now()))
SESSION = requests.Session()

print('{0} - Startup complete'.format(datetime.now()))

while True:
  try:
    reading = SENSOR.sample(samples=int(SENSOR_SAMPLES))

    if DASHBOARD:
      payload = {'func': 'putReading', 'key': DASHBOARD_KEY, 'temperature': reading['temp_c'], 'humidity': reading['humidity']}
      # TODO: Store both temp_c and temp_f
      # payload = {'func': 'putReading', 'key': DASHBOARD_KEY, 'temp_c': reading['temp_c'], 'temp_f': reading['temp_f'], 'humidity': reading['humidity']}

      try:
        SESSION.post(DASHBOARD_HOST + '/src/action.php', data=payload, timeout=5.0)
      except requests.exceptions.RequestException as exception:
        print('{0} - {1}'.format(datetime.now(), exception))
    else:
      print('{0} - Temperature={1:0.2f}°C ({2:0.2f}°F), Humidity={3:0.2f}%'.format(datetime.now(), reading['temp_c'], reading['temp_f'], reading['humidity']))

    sleep(float(SENSOR_FREQUENCY))
  except TimeoutError as exception:
      print('{0} - {1}'.format(datetime.now(), exception))
      sleep(2)
