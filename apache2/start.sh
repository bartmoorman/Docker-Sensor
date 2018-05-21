#!/bin/sh
groupadd -fg $(stat -c '%g' /sys/class/gpio/) gpio
usermod -aG gpio apache

chown apache: /config

if [ ! -d /config/httpd/ssl ]; then
    mkdir -p /config/httpd/ssl
    ln -sf /etc/ssl/apache2/server.pem /config/httpd/ssl/sensor.crt
    ln -sf /etc/ssl/apache2/server.key /config/httpd/ssl/sensor.key
fi

pidfile=/var/run/apache2/httpd.pid

if [ -f ${pidfile} ]; then
    pid=$(cat ${pidfile})

    if [ ! -d /proc/${pid} ] || [[ -d /proc/${pid} && $(basename $(readlink /proc/${pid}/exe)) != 'httpd' ]]; then
      rm ${pidfile}
    fi
elif [ ! -d /var/run/apache2 ]; then
    mkdir -p /var/run/apache2
fi

$(which apachectl) \
    -D ${HTTPD_SECURITY:-HTTPD_SSL} \
    -D ${HTTPD_REDIRECT:-HTTPD_REDIRECT_SSL}

exec $(which sensor)
