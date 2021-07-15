FROM python:3.7-slim

WORKDIR /usr/src/api
COPY . .

RUN pip install -r requirements.txt \
    && rm -rf /root/.cache/pip