FROM python:3.7-slim

WORKDIR /usr/src/workflow

COPY requirements.txt ./

RUN pip install -r requirements.txt \
    && rm -rf /root/.cache/pip

COPY . .

EXPOSE 5000

ENTRYPOINT ["uvicorn", "endpoint:app", "--port=5000", "--host", "0.0.0.0"]