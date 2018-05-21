## This is designed for a Raspberry Pi Zero W

### Usage
```
docker run \
--detach \
--name sensor \
--publish 2876:2876 \
--env "HTTPD_SERVERNAME=**sub.do.main**" \
--volume /sys:/sys \
--volume sensor-config:/config \
bmoorman/sensor:latest
```
