FROM python:3.8

MAINTAINER Alix Boc <dcarrey@gmail.com>

COPY . /opt/app

WORKDIR /opt/app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt
