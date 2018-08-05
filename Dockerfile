FROM bmoorman/alpine:armhf

ENV DHT_PIN="17" \
    DHT_TYPE="DHT22"

WORKDIR /opt/Adafruit_Python_DHT

COPY Adafruit_Python_DHT .

RUN apk add --no-cache \
    python \
    py-requests \
    py-setuptools \
 && apk add --no-cache --virtual .build-deps \
    build-base \
    python-dev \
 && python setup.py install \
 && apk del --no-cache .build-deps

COPY bin/ /usr/local/bin/

CMD ["sensor.py"]
