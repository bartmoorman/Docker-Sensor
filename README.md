## This is designed for a Raspberry Pi

### Docker Run
```
docker run \
--detach \
--name sensor \
--privileged \
--env "DASHBOARD_HOST=https://**sub.do.main**" \
--env "DASHBOARD_KEY=da03bc3094b83de7" \
bmoorman/sensor:armhf-latest
```

### Docker Compose
```
version: "3.7"
services:
  sensor:
    image: bmoorman/sensor:armhf-latest
    container_name: sensor
    environment:
      - DASHBOARD_HOST=https://**sub.do.main**
      - DASHBOARD_KEY=da03bc3094b83de7
    privileged: true
```
