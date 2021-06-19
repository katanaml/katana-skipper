# Katana ML Skipper Workflow API

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

4. Web API FastAPI endpoint

URL: http://127.0.0.1:8000/docs

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
