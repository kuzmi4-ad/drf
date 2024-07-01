#!/bin/sh

python manage.py collectstatic --no-input --clear
gunicorn drf.wsgi:application --bind 0.0.0.0:8000