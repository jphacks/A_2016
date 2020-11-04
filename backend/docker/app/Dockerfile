FROM python:3.9-alpine

WORKDIR /app

RUN apk --no-cache --update-cache add \
    gcc \
    gfortran \
    build-base \
    wget \
    freetype-dev \
    libpng-dev \
    openblas-dev \
    postgresql-dev \
    musl-dev

COPY requirements.txt /

RUN pip install --no-cache-dir -r /requirements.txt

COPY . /app

CMD make start-prod
