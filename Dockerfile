FROM python:3.7-slim

ENV PYTHONUNBUFFERED 1

ARG DEBIAN_FRONTEND=noninteractive

#COPY etc/oracle/instantclient-basiclite-linux.x64-18.3.0.0.0dbru.zip /tmp/instantclient-basiclite-linux.x64-18.3.0.0.0dbru.zip

RUN apt-get update \
    && apt-get install -y dialog apt-utils gcc



COPY requirements.txt /code/requirements.txt

WORKDIR /code

RUN pip install --upgrade pip && pip install -r /code/requirements.txt

RUN mkdir /static/ /media_app/

VOLUME /static/

VOLUME /media_app/

EXPOSE 8000

ENV DATABASE_URL=none

# Add any custom, static environment variables needed by Django or your settings file here 9default production settings)
# TODO: check wsgi.py - it is overridden there !!!

ENV DJANGO_SETTINGS_MODULE=settings.production

# uWSGI configuration (customize as needed)
ENV UWSGI_WSGI_FILE=/code/wsgi.py UWSGI_SOCKET=:8000 UWSGI_MASTER=1 UWSGI_WORKERS=2 UWSGI_THREADS=8 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy

COPY . /code/

ENTRYPOINT ["/code/docker-entrypoint.sh"]

# Start uWSGI
CMD ["/usr/local/bin/uwsgi"]
