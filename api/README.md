# Katana ML Skipper Web API

Web API implements external access endpoints. Clients can trigger actions in the workflow through this API. It runs async and sync endpoints. Async endpoint is executed through Celery Distributed Queue. When async task is started, API returns task ID. Using this task ID, we can check task status and get result when ready. Sync task sends event through RabbitMQ RPC and waits for the response.

To make the API generic, there is a Worklow service, called through Requests. Based on request type, it returns queue name, where event should be sent.

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
uvicorn endpoint:app --reload
```

3. Start Celery task distributed queue

```
celery -A api.worker worker --loglevel=INFO
```

4. Web API FastAPI endpoints

```
http://localhost:8000/api/v1/skipper/tasks/docs
```

#### Build individual container

1. Build container

```
docker build --tag katanaml/skipper-api .
```

```
docker build --tag katanaml/skipper-api-celery .
```

#### Build and run Kubernetes Pod for API

1. Create namespace

```
kubectl create ns katana-skipper
```

2. Create Pod

```
kubectl apply -n katana-skipper -f api-pod.yaml
```

3. Check Pod status

```
kubectl get -n katana-skipper pods
```

4. Describe Pod

```
kubectl describe -n katana-skipper pods skipper-api
```

5. Open Pod port for testing purposes

```
kubectl port-forward -n katana-skipper deploy/skipper-api 8000:8000
```

6. Open Pod logs

```
kubectl logs -n katana-skipper -f -l app=skipper-api
```

7. Test URL

```
http://localhost:8000/api/v1/skipper/tasks/docs
```

8. Check Pod service

```
kubectl get -n katana-skipper svc skipper-api
```

9. Delete Deployment

```
kubectl delete -n katana-skipper -f api-pod.yaml
```

10. Delete all resources

```
kubectl delete all --all -n katana-skipper
```

#### Build and run Kubernetes Pod for API Celery

1. Create namespace

```
kubectl create ns katana-skipper
```

2. Create Pod

```
kubectl apply -n katana-skipper -f api-celery-pod.yaml
```

3. Check Pod status

```
kubectl get -n katana-skipper pods
```

4. Describe Pod

```
kubectl describe -n katana-skipper pods skipper-api-celery
```

5. Open Pod logs

```
kubectl logs -n katana-skipper -f -l app=skipper-api-celery
```

6. Delete Deployment

```
kubectl delete -n katana-skipper -f api-celery-pod.yaml
```

7. Delete all resources

```
kubectl delete all --all -n katana-skipper
```

## Structure

```
.
├── api 
│   ├── models.py
│   ├── tasks.py
│   ├── dependencies.py
├── ├──routers
│       ├── boston.py
│       ├── mobilenet.py
│       └── skipper.py
│   └── worker.py
├── endpoint.py
├── Dockerfile
├── README.md
├── api-pod.yaml
├── api-celery-pod.yaml
├── api-ingress.yaml
└── requirements.txt
```

## License

Licensed under the Apache License, Version 2.0. Copyright 2020-2021 Katana ML, Andrej Baranovskij. [Copy of the license](https://github.com/katanaml/katana-skipper/blob/master/LICENSE).
