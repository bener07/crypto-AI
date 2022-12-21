#!/bin/bash
gunicorn --config /app/gunicorn_config.py --log-level=info wsgi:app
