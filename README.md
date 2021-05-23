# Katana ML Skipper
[![GitHub Stars](https://img.shields.io/github/stars/katanaml/katana-skipper.svg?style=for-the-badge)](https://github.com/katanaml/katana-skipper/stargazers) [![GitHub Issues](https://img.shields.io/github/issues/katanaml/katana-skipper.svg)](https://github.com/katanaml/katana-skipper/issues) [![Current Version](https://img.shields.io/badge/version-21.1-green.svg)](https://github.com/katanaml/katana-skipper)

This is a simple and flexible ML workflow engine. It helps to orchestrate events across a set of microservices and create executable flow to handle requests. Engine is designed to be configurable with any microservises. Enjoy!

![Skipper](https://github.com/katanaml/katana-skipper/blob/master/skipper.png)

## Author

Katana ML, Red Samurai Consulting, Andrej Baranovskij

## Instructions

### Start/Stop

* docker-compose up --build -d
* docker-compose down

### Components

* **[engine](https://github.com/katanaml/katana-skipper/tree/master/engine)** - workflow implementation
* **[services](https://github.com/katanaml/katana-skipper/tree/master/services)** - a set of microservices
* **rabbitmq** - service for RabbitMQ broker

### URLs

* RabbitMQ: http://localhost:15672/ (skipper/welcome1)

## License

Licensed under the Apache License, Version 2.0. Copyright 2020-2021 Katana ML. [Copy of the license](https://github.com/katanaml/katana-pipeline/blob/master/LICENSE).
