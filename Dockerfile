FROM bmoorman/alpine:armhf

ENV DHT_PIN="17" \
    DHT_TYPE="DHT22"

RUN apk add --no-cache \
    python \
    py-requests \
    py-setuptools \
 && apk add --no-cache --virtual .build-deps \
    g++ \
    git \
    python-dev \
 && git clone https://github.com/adafruit/Adafruit_Python_DHT.git \
 && cd Adafruit_Python_DHT \
 && python setup.py install \
 && apk del --no-cache .build-deps \
 && rm -rf Adafruit_Python_DHT

COPY bin/ /usr/local/bin/

CMD ["sensor.py"]
