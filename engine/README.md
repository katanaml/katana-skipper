# Katana ML Skipper Workflow Engine

## Author

Katana ML, Andrej Baranovskij

## Instructions

1. Install libraries

```
pip install -r requirements.txt
```

2. Start FastAPI

```
uvicorn endpoint:app --reload
```

3. Start Celery task distributed queue

```
celery -A api.worker worker --loglevel=INFO
```

4. Optional - start RabbitMQ test receiver

```
python event_receiver_test.py
```

5. Web API FastAPI endpoint

URL: http://127.0.0.1:8000/docs

## Structure

```
.
├── api 
│   ├── backend
│       ├── event_producer.py
│       └── event_receiver.py
│   ├── models.py
│   ├── router.py
│   ├── tasks.py
│   └── worker.py
├── endpoint.py
├── README.md
└── requirements.txt
```

## License

Licensed under the Apache License, Version 2.0. Copyright 2020-2021 Katana ML, Andrej Baranovskij. [Copy of the license](https://github.com/katanaml/katana-pipeline/blob/master/LICENSE).
