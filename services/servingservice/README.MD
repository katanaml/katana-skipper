# Katana ML Skipper Serving Service

## Author

Katana ML, Andrej Baranovskij

## Instructions

To run all services, check instructions in main [README](https://github.com/katanaml/katana-skipper/blob/master/README.md)

#### Run the service without Docker

1. Install libraries

```
pip install -r requirements.txt
```

2. Start service

```
python main.py
```

#### Build and run individual container

1. Build container

```
docker build --tag katanaml/serving-service .
```

2. Run container

```
docker run -it -d --name serving-service -p 5001:5001  katanaml/serving-service:latest
```

## Structure

```
.
├── app 
│   └── serving_service.py
├── main.py
├── Dockerfile
├── README.md
└── requirements.txt
```

## License

Licensed under the Apache License, Version 2.0. Copyright 2020-2021 Katana ML, Andrej Baranovskij. [Copy of the license](https://github.com/katanaml/katana-pipeline/blob/master/LICENSE).
