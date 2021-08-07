FROM python:3.7-slim

WORKDIR /usr/src/dataservice

COPY requirements.txt ./

RUN pip install -r requirements.txt \
    && rm -rf /root/.cache/pip

COPY . .

ENTRYPOINT ["python", "main.py"]