#!/bin/sh

set -e

if [ "$1" = "/usr/local/bin/uwsgi" ]; then
    python manage.py collectstatic --noinput
    sleep 5
    python manage.py migrate --noinput
fi

exec "$@"
