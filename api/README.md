# Katana ML Skipper Web API

Web API implements external access endpoints. Clients can trigger actions in the workflow through this API. It runs async and sync endpoints. Async endpoint is executed through Celery Distributed Queue. When async task is started, API returns task ID. Using this task ID, we can check task status and get result when ready. Sync task sends event through RabbitMQ RPC and waits for the response.

To make the API generic, there is a Worklow service, called through Requests. Based on request type, it returns queue name, where event should be sent.

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

4. Web API FastAPI endpoints

```
URL: http://127.0.0.1:8000/docs
```

## Structure

```
.
├── api 
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
