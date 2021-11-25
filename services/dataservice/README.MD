# Katana ML Skipper Data Service

## Author

[Katana ML](https://katanaml.io), [Andrej Baranovskij](https://github.com/abaranovskis-redsamurai)

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

Licensed under the Apache License, Version 2.0. Copyright 2020-2021 Katana ML, Andrej Baranovskij. [Copy of the license](https://github.com/katanaml/katana-skipper/blob/master/LICENSE).
