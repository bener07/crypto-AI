#!/bin/sh
if [ $SERVER_HOST_PORT ]
then
    echo "Using port: $SERVER_HOST_PORT\n";
else
    echo "Using default port 8000";
    SERVER_HOST_PORT = "0.0.0.0:8000";
fi
python3 manage.py runserver $SERVER_HOST_PORT