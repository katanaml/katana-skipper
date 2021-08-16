# Katana ML Skipper Logger

Logger service, logging runs in the background, without blocking API endpoint

## Author

Katana ML, Andrej Baranovskij

## Instructions

Use Docker Compose to run all services, check main [README](https://github.com/katanaml/katana-skipper/blob/master/README.md)

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
kubectl apply -f logger-pod.yaml
```

3. Check Pod status

```
kubectl get pods
```

4. Describe Pod

```
kubectl describe pods skipper-logger
```

5. Open Pod port for testing purposes

```
kubectl port-forward deploy/skipper-logger 5001:5001
```

6. Open Pod logs

```
kubectl logs -f -l app=skipper-logger
```

7. Test URL

```
http://127.0.0.1:5001/docs
```

8. Check Pod service

```
kubectl get svc skipper-logger
```

9. Delete Pod, if not needed

```
kubectl delete -f logger-pod.yaml
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

Licensed under the Apache License, Version 2.0. Copyright 2020-2021 Katana ML, Andrej Baranovskij. [Copy of the license](https://github.com/katanaml/katana-pipeline/blob/master/LICENSE).
