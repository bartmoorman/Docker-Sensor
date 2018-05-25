FROM bmoorman/alpine:armhf

ENV SENSOR_PIN="17" \
    SENSOR_TYPE="DHT22" \
    THINGSPEAK_API_KEY="" \
    THINGSPEAK_TEMP_C="field1" \
    THINGSPEAK_TEMP_F="field2" \
    THINGSPEAK_HUMIDITY="field3"

RUN apk add --no-cache \
    python \
    py-requests \
    py-setuptools \
 && apk add --no-cache --virtual _build \
    g++ \
    git \
    python-dev \
 && git clone https://github.com/adafruit/Adafruit_Python_DHT.git \
 && cd Adafruit_Python_DHT \
 && python setup.py install \
 && apk del --no-cache _build \
 && rm -rf Adafruit_Python_DHT

COPY bin/ /usr/local/bin/

CMD ["sensor.py"]
