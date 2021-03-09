FROM bmoorman/alpine:armhf-3.8

RUN apk add --no-cache \
    python \
    py-requests \
 && apk add --no-cache --virtual .build-deps \
    build-base \
    py-pip \
    python-dev \
 && pip install Adafruit-DHT \
 && apk del --no-cache .build-deps

COPY bin/ /usr/local/bin/

CMD ["sensor.py"]
