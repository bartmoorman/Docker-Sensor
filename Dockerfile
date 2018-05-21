FROM bmoorman/alpine:armhf

ENV HTTPD_SERVERNAME="localhost" \
    SENSOR_PIN="17" \
    SENSOR_TYPE="DHT22"

RUN apk add --no-cache \
    apache2 \
    apache2-ctl \
    apache2-ssl \
    curl \
    php7 \
    php7-apache2 \
    php7-json \
    php7-session \
    php7-sqlite3 \
    python \
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

COPY apache2/ /etc/apache2/
COPY htdocs/ /var/www/localhost/htdocs/
COPY bin/ /usr/local/bin/

VOLUME /config

EXPOSE 2876

CMD ["/etc/apache2/start.sh"]

HEALTHCHECK --interval=60s --timeout=5s CMD curl --silent --location --fail http://localhost:80/ > /dev/null || exit 1
