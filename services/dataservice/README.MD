# Katana ML Skipper Data Service

## Author

Katana ML, Andrej Baranovskij

## Instructions

Use Docker Compose to run all services, check main [README](https://github.com/katanaml/katana-skipper/blob/master/README.md)

#### Use below instructions, if you choose to run the service without Docker.

1. Install libraries

```
pip install -r requirements.txt
```

2. Start service

```
python main.py
```

#### Use below instructions to build and run individual container:

1. Build container

```
docker build --tag katanaml/data-service .
```

2. Run container

```
docker run -it -d --name data-service katanaml/data-service:latest
```

## Structure

```
.
├── app 
│   └── data_service.py
├── main.py
├── Dockerfile
├── README.md
└── requirements.txt
```

## License

Licensed under the Apache License, Version 2.0. Copyright 2020-2021 Katana ML, Andrej Baranovskij. [Copy of the license](https://github.com/katanaml/katana-pipeline/blob/master/LICENSE).
