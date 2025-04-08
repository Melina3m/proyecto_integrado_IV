FROM python:3.8.13 as base
FROM ubuntu
RUN apt-get update
RUN apt-get install -y python3