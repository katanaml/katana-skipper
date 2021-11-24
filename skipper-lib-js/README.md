# @katanaml/skipper-lib-js

[![npm (scoped)](https://img.shields.io/npm/v/@katanaml/skipper-lib-js.svg)](https://www.npmjs.com/package/@katanaml/skipper-lib-js)

## Overview

This is a helper library for Katana ML Skipper workflow product. The idea of this library is to wrap all reusable code to simplify and improve workflow implementation.

Supported functionality:

- API to communicate with RabbitMQ for event receiver/producer

## Author

Katana ML, Andrej Baranovskij

## Install

```
$ npm install @bamblehorse/tiny
```

## Usage

```js
// Receiver
var event_receiver = new EventReceiver(RABBITMQ_USER, 
                                       RABBITMQ_PASSWORD, 
                                       RABBITMQ_HOST, 
                                       RABBITMQ_PORT, 
                                       QUEUE_NAME,
                                       SERVICE_NAME);
event_receiver.startListener(event_receiver.onRequest, new MobilenetService(), LOGGER_RECEIVER_URL);

// Producer
var event_producer = new EventProducer(
            RABBITMQ_USER,
            RABBITMQ_PASSWORD,
            RABBITMQ_HOST,
            RABBITMQ_PORT);

        var data = {
            'task_type': 'training',
            'payload': '0.2',
            'description': 'string'
        }
        data = JSON.stringify(data);
        event_producer.call(this.processResponse, data, LOGGER_RECEIVER_URL, QUEUE_NAME_DATA, SERVICE_NAME);
```

## Structure

```
.
├── LICENSE
├── poetry.lock
├── pyproject.toml
├── skipper_lib
│   ├── __init__.py
│   ├── __main__.py
│   ├── events
│       ├── __init__.py
│       ├── exchange_producer.py
│       ├── exchange_receiver.py
│       ├── event_producer.py
│       └── event_receiver.py
│   ├── logger
│       ├── __init__.py
│       └── logger_helper.py
│   ├── workflow
│       ├── __init__.py
│       └── workflow_helper.py
└── README.md
```

## License

Licensed under the Apache License, Version 2.0. Copyright 2020-2021 Katana ML, Andrej Baranovskij. [Copy of the license](https://github.com/katanaml/katana-pipeline/blob/master/LICENSE).
