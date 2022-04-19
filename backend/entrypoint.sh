#!/bin/sh

gunicorn -w "${GUNICORN_WORKERS:-3}" -b "${GUNICORN_BIND:-0.0.0.0:5000}" wsgi:app