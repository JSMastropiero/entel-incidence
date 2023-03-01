FROM python:3.10.9-alpine3.16

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./app /app

WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home app

RUN apk add --no-cache openjdk11 && \
    wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-7.16.3-linux-x86_64.tar.gz && \
    tar -xzf elasticsearch-7.16.3-linux-x86_64.tar.gz && \
    rm elasticsearch-7.16.3-linux-x86_64.tar.gz && \
    mv elasticsearch-7.16.3 /usr/share/elasticsearch

ENV PATH="/py/bin:/usr/share/elasticsearch/bin:$PATH"

USER app