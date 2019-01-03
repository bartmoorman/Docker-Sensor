## This is designed for a Raspberry Pi

### Usage
```
docker run \
--detach \
--name sensor \
--privileged \
--env "DASHBOARD_HOST=**sub.do.main**" \
--env "DASHBOARD_KEY=da03bc3094b83de7"
bmoorman/sensor:latest
```
