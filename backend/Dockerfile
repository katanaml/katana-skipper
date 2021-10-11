FROM python:3.7-slim

WORKDIR /usr/src/backend

COPY requirements.txt ./

RUN pip install -r requirements.txt \
    && rm -rf /root/.cache/pip

COPY . .

EXPOSE 8000


ENTRYPOINT ["uvicorn", "main:app", "--port=9999", "--host", "0.0.0.0", "--reload"]