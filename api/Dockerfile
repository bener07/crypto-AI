FROM ubuntu:latest
RUN apt-get update && apt-get install gunicorn python3 python3-pip -y
RUN pip install flask requests flask-cors
WORKDIR /app
ENTRYPOINT gunicorn --bind 0.0.0.0:5000 wsgi:app
