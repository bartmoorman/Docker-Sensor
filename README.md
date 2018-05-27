## This is designed for a Raspberry Pi Zero W

### Usage
```
docker run \
--detach \
--name sensor \
--privileged \
--env "DASHBOARD_HOST=**sub.do.main**" \
--env "DASHBOARD_TOKEN=da03bc3094b83de7"
bmoorman/sensor:latest
```
