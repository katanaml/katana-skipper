# Katana ML Skipper Logger

Logger service, logging runs in the background, without blocking API endpoint.

## Author

[Katana ML](https://katanaml.io), [Andrej Baranovskij](https://github.com/abaranovskis-redsamurai)

## Instructions

To run all services, check instructions in main [README](https://github.com/katanaml/katana-skipper/blob/master/README.md)

#### Run the service without Docker

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
http://127.0.0.1:5001/docs
```

4. Monitor logs

```
docker logs --follow skipper-logger
```

#### Build and run individual container

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
http://127.0.0.1:5001/docs
```

4. Monitor logs

```
docker logs --follow skipper-logger
```

#### Build and run Kubernetes Pod

1. Create namespace

```
kubectl create ns katana-skipper
```

2. Create Pod

```
kubectl apply -n katana-skipper -f logger-pod.yaml
```

3. Check Pod status

```
kubectl get -n katana-skipper pods
```

4. Describe Pod

```
kubectl describe -n katana-skipper pods skipper-logger
```

5. Open Pod port for testing purposes

```
kubectl port-forward -n katana-skipper deploy/skipper-logger 5001:5001
```

6. Open Pod logs

```
kubectl logs -n katana-skipper -f -l app=skipper-logger
```

7. Test URL

```
http://127.0.0.1:5001/docs
```

8. Check Pod service

```
kubectl get -n katana-skipper svc skipper-logger
```

9. Delete Deployment

```
kubectl delete -n katana-skipper -f logger-pod.yaml
```

10. Delete all resources

```
kubectl delete all --all -n katana-skipper
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
├── logger-pod.yaml
└── requirements.txt
```

## License

Licensed under the Apache License, Version 2.0. Copyright 2020-2021 Katana ML, Andrej Baranovskij. [Copy of the license](https://github.com/katanaml/katana-skipper/blob/master/LICENSE).
