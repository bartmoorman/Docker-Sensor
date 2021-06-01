Gather environment readings for [Sensor Dashboard](https://github.com/iVirus/Docker-Sensor-Dashboard)

### Docker Run
```
docker run \
--detach \
--name sensor \
--restart unless-stopped \
--privileged \
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
    privileged: true
```

### Environment Variables
|Variable|Description|Default|
|--------|-----------|-------|
|TZ|Sets the timezone|`America/Denver`|
|DASHBOARD_HOST|Sets the Dashboard host|`<empty>`|
|DASHBOARD_KEY|Sets the Dashboard key for this sensor|`<empty>`|
|DHT_TYPE|Sets the attached sensor type (`DHT11`, `DHT22`, or `AM2302`)|`DHT22`|
|DHT_PIN|Sets the BCM pin where the environment sensor is attached|`D17`|
|FREQUENCY|Sets how often to collect (and send) readings [seconds]|`30`|
