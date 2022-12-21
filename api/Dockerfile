FROM ubuntu:latest
RUN apt-get update && apt-get install gunicorn python3 python3-pip -y
COPY app/requirements.txt /tmp/
COPY entrypoint.sh /
RUN pip install -r tmp/requirements.txt
WORKDIR /app
EXPOSE 5000
ENTRYPOINT ["/entrypoint.sh"]
