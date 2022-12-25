#!/bin/sh
if [ $SERVER_HOST_PORT ]
then
    echo "Using port: $SERVER_HOST_PORT\n";
else
    echo "Using default port 8000";
    SERVER_HOST_PORT = 8000;
fi
echo $SERVER_HOST_PORT
python3 manage.py runserver $SERVER_HOST_PORT