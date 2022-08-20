FROM python:3.9-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .

RUN apk update \
    && apk add --virtual .tmp gcc python3-dev musl-dev postgresql-dev jpeg-dev zlib-dev \
    && apk add libjpeg \
    && pip install --upgrade pip  \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .tmp
