# Katana ML Skipper
[![GitHub Stars](https://img.shields.io/github/stars/IgorAntun/node-chat.svg)](https://github.com/IgorAntun/node-chat/stargazers)

This is a simple and flexible ML workflow engine. It helps to orchestrate events across a set of microservices and create executable flow to handle requests. Engine is designed to be configurable with any microservises. Enjoy!

![Skipper](https://github.com/katanaml/katana-skipper/blob/master/skipper.png)

## Author

Katana ML, Red Samurai Consulting, Andrej Baranovskij

## Instructions

### Start/Stop

* docker-compose up --build -d
* docker-compose down

### Components

* **engine** - workflow implementation
* **services** - a set of microservices
* **rabbitmq** - service for RabbitMQ broker

### URLs

* RabbitMQ: http://localhost:15672/ (skipper/welcome1)

## License

Licensed under the Apache License, Version 2.0. Copyright 2020-2021 Katana ML. [Copy of the license](https://github.com/katanaml/katana-pipeline/blob/master/LICENSE).
