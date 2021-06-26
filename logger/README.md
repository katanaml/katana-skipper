# Katana ML Skipper Logger

Logger service, logging runs in the background, without blocking API endpoint

## Author

Katana ML, Andrej Baranovskij

## Instructions

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


## Structure

```
.
├── api 
│   ├── logger.py
│   ├── models.py
│   └── router.py
├── endpoint.py
├── README.md
└── requirements.txt
```

## License

Licensed under the Apache License, Version 2.0. Copyright 2020-2021 Katana ML, Andrej Baranovskij. [Copy of the license](https://github.com/katanaml/katana-pipeline/blob/master/LICENSE).
