#!/bin/sh
if [ $SERVER_PORT ]
then
    echo "Using port: $SERVER_PORT\n";
else
    echo "Using default port 8000";
    SERVER_PORT = 8000;
fi
echo $SERVER_PORT
python3 manage.py runserver $SERVER_PORT