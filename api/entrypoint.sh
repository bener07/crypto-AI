#!/bin/bash
gunicorn --config /app/gunicorn_config.py wsgi:app
