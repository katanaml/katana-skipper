FROM python:3.7-slim

WORKDIR /usr/src/logger

COPY requirements.txt ./

RUN pip install -r requirements.txt \
    && rm -rf /root/.cache/pip

COPY . .

EXPOSE 5001

ENTRYPOINT ["uvicorn", "endpoint:app", "--port=5001", "--host", "0.0.0.0"]