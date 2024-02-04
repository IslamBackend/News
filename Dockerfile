FROM python:3.12

ENV PYTHONWRITEBYCODE 1
ENV PYTHONBUFFERED 1

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r /app/requirements.txt

COPY . /app
