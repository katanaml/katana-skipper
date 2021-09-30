FROM python:3.7-slim

WORKDIR /usr/src/servingservice/storage

COPY requirements.txt ./

RUN pip install -r requirements.txt \
    && rm -rf /root/.cache/pip

COPY . .

ENTRYPOINT ["python", "storage_controller.py"]