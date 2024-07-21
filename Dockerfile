# Use the official Python base image
FROM python:3.12.1

WORKDIR /my_portfolio

COPY requirements.txt /my_portfolio/

RUN pip install -r requirements.txt
RUN pip install whitenoise

COPY . /my_portfolio/