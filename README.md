Gather environment readings for [Sensor Dashboard](https://github.com/iVirus/Docker-Sensor-Dashboard)

### Docker Run
```
docker run \
--detach \
--name sensor \
--restart unless-stopped \
bmoorman/sensor:armhf-latest
```

### Docker Compose
```
version: "3.7"
services:
  sensor:
    image: bmoorman/sensor:armhf-latest
    container_name: sensor
    restart: unless-stopped
```

### Environment Variables
|Variable|Description|Default|
|--------|-----------|-------|
|TZ|Sets the timezone|`America/Denver`|
|DASHBOARD_HOST|Sets the Dashboard host|`<empty>`|
|DASHBOARD_KEY|Sets the Dashboard key for this sensor|`<empty>`|
|SENSOR_TYPE|Sets the attached sensor type (`DHT11`, `DHT22`, or `AM2302`)|`DHT22`|
|SENSOR_PIN|Sets the BCM pin where the sensor is attached|`17`|
|SENSOR_SAMPLES|Sets how many samples to collect from the sensor [normalized]|`5`|
|SENSOR_FREQUENCY|Sets how long to wait before resampling (seconds)|`5`|
|SENSOR_TIMEOUT|Sets how long to wait for a response from the sensor (seconds)|`0.5`|
|PIGPIO_ADDR|Sets the host of pigpiod|`localhost`|
|PIGPIO_PORT|Sets the port of pigpiod|`8888`|
