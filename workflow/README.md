# Katana ML Skipper Workflow

Returns queue name, based on task ID. This allows to route event to the correct queue, without hardcoding logic in the Web API.

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
uvicorn endpoint:app --port=5000 --reload
```

3. Workflow FastAPI endpoints

```
http://127.0.0.1:5000/docs
```

#### Build and run individual container

1. Build container

```
docker build --tag katanaml/skipper-workflow .
```

2. Run container

```
docker run -it -d --name skipper-workflow -p 5000:5000  katanaml/skipper-workflow:latest
```

3. Logger FastAPI endpoints

```
http://127.0.0.1:5000/docs
```

#### Build and run Kubernetes Pod

1. Create Pod

```
kubectl apply -f workflow-pod.yaml
```

2. Check Pod status

```
kubectl get pods
```

3. Describe Pod

```
kubectl describe pods skipper-workflow
```

4. Open Pod port for testing purposes

```
kubectl port-forward deploy/skipper-workflow 5000:5000
```

5. Open Pod logs

```
kubectl logs -f -l app=skipper-workflow
```

6. Test URL

```
http://127.0.0.1:5000/docs
```

7. Delete Pod, if not needed

```
kubectl delete -f workflow-pod.yaml
```

8. Check Pod service

```
kubectl get svc skipper-workflow
```


## Structure

```
.
├── api 
│   ├── models.py
│   ├── router.py
│   ├── workflow.json
│   └── workflow.py
├── endpoint.py
├── Dockerfile
├── README.md
├── workflow-pod.yaml
└── requirements.txt
```

## License

Licensed under the Apache License, Version 2.0. Copyright 2020-2021 Katana ML, Andrej Baranovskij. [Copy of the license](https://github.com/katanaml/katana-pipeline/blob/master/LICENSE).
