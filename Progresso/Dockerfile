FROM python:3.11.5-slim-bullseye

ENV PYTHONUNBUFFERED 1

WORKDIR /Progresso

ADD . /Progresso

COPY ./requirements.txt /Progresso/requirements.txt


RUN pip install -r requirements.txt

COPY . /Progresso