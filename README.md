## This is designed for a Raspberry Pi Zero W

### Usage
```
docker run \
--detach \
--name sensor \
--privileged \
--env "THINGSPEAK_API_KEY=**channel api key**" \
bmoorman/sensor:latest
```
