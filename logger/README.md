# Katana ML Skipper Logger

Logger service, logging runs in the background, without blocking API endpoint

## Author

Katana ML, Andrej Baranovskij

## Instructions

Use Docker Compose to run all services, check main [README](https://github.com/katanaml/katana-skipper/blob/master/README.md)

Use below instructions, if you choose to run the service without Docker.

1. Install libraries

```
pip install -r requirements.txt
```

2. Start FastAPI

```
uvicorn endpoint:app --port=5001 --reload
```

3. Logger FastAPI endpoints

```
URL: http://127.0.0.1:5001/docs
```

Use below instructions to build and run individual container:

1. Build container

```
docker build --tag katanaml/skipper-logger .
```

2. Run container

```
docker run -it -d --name skipper-logger -p 5001:5001  katanaml/skipper-logger:latest
```

3. Logger FastAPI endpoints

```
URL: http://127.0.0.1:5001/docs
```


## Structure

```
.
├── api 
│   ├── logger.py
│   ├── models.py
│   └── router.py
├── endpoint.py
├── Dockerfile
├── README.md
└── requirements.txt
```

## License

Licensed under the Apache License, Version 2.0. Copyright 2020-2021 Katana ML, Andrej Baranovskij. [Copy of the license](https://github.com/katanaml/katana-pipeline/blob/master/LICENSE).
