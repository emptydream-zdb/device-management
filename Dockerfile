FROM python:3.9.17-slim-bullseye

WORKDIR /app

COPY requirements.txt ./requirements.txt 

RUN pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/

COPY . .
