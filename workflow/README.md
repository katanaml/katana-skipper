# Katana ML Skipper Workflow

Returns queue name, based on task ID. This allows to route event to the correct queue, without hardcoding logic in the Web API.

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
uvicorn endpoint:app --port=5000 --reload
```

3. Workflow FastAPI endpoints

```
URL: http://127.0.0.1:5000/docs
```


## Structure

```
.
├── api 
│   ├── models.py
│   ├── router.py
│   ├── workflow.json
│   └── workflow.py
├── endpoint.py
├── Dockerfile
├── README.md
└── requirements.txt
```

## License

Licensed under the Apache License, Version 2.0. Copyright 2020-2021 Katana ML, Andrej Baranovskij. [Copy of the license](https://github.com/katanaml/katana-pipeline/blob/master/LICENSE).
