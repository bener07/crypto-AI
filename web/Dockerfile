FROM python:latest
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
WORKDIR /app
COPY entrypoints /entrypoints
RUN if [ $PRODUCTION ]; then mv /entrypoints/entrypoint-production.sh /entrypoints/entrypoint.sh; else echo "Using development server";fi
EXPOSE 8000
ENTRYPOINT [ "/entrypoints/entrypoint.sh" ]