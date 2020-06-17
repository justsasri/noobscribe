# pull official base image
FROM python:3.7-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY . .
RUN python -m pip install --upgrade pip
RUN pip install pipenv
RUN pipenv shell
RUN pipenv install --skip-lock