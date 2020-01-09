FROM python:3.7

WORKDIR /app

ENV LISTEN_PORT 5000

COPY requirements.txt /tmp
RUN pip install -r /tmp/requirements.txt

RUN useradd -m deploy

EXPOSE 5000
ENTRYPOINT ["/app/dev/entrypoint.sh"]