# Katana ML Skipper Mobilenet Service

## Author

Katana ML, Andrej Baranovskij

## Instructions

This is a sample service implementation with JavaScript

To run all services, check instructions in main [README](https://github.com/katanaml/katana-skipper/blob/master/README.md)


#### Run the service without Docker

1. Install node module for Skipper library:

```
npm install --save @katanaml/skipper-lib-js
```

2. Start service

```
node src/main.js
```


#### Build and run individual container


#### Build and run Kubernetes Pod


## Structure

```
.
├── src
│   └── app
│       └── mobilenet_service.js
├──── main.js
├── Dockerfile
├── README.md
├── package-lock.json
└── package.json
```

## License

Licensed under the Apache License, Version 2.0. Copyright 2020-2021 Katana ML, Andrej Baranovskij. [Copy of the license](https://github.com/katanaml/katana-pipeline/blob/master/LICENSE).
