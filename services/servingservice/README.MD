# Katana ML Skipper Serving Service

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

3. Start storage service

```
python storage_controller.py
```

#### Build and run individual container

1. Build container

```
docker build --tag katanaml/serving-service .
```

2. Run container

```
docker run -it -d --name serving-service katanaml/serving-service:latest
```

#### Build and run Kubernetes Pod

1. Create namespace

```
kubectl create ns katana-skipper
```

2. Check available storage class

```
kubectl get storageclass
```

3. Create volume

```
kubectl apply -f servingservice-pv.yaml
```

4. Create volume claim

```
kubectl apply -n katana-skipper -f servingservice-pvc.yaml
```

5. Create Pod

```
kubectl apply -n katana-skipper -f servingservice-pod.yaml
```

6. Check Pod status

```
kubectl get -n katana-skipper pods
```

7. Open Pod logs, use storage-service for sidecar container logs

```
kubectl logs -n katana-skipper -f -l app=serving-service -c serving-main-service
```

or

```
kubectl logs -n katana-skipper -f <POD_NAME> -c serving-main-service
```

8. Check volume

```
kubectl get pv
```

9. Check volume claim

```
kubectl get -n katana-skipper pvc
```

10. Execute commands inside container

```
kubectl exec -it -n katana-skipper <POD_NAME> -c serving-main-service -- bash
```

11. Scale Pod

```
kubectl scale -n katana-skipper deployment serving-service --replicas=3
```

12. Delete Deployment and Volumes

```
kubectl delete -n katana-skipper -f servingservice-pod.yaml
```

```
kubectl delete -n katana-skipper -f servingservice-pvc.yaml
```

```
kubectl delete -f servingservice-pv.yaml
```

13. Delete all resources

```
kubectl delete all --all -n katana-skipper
```

## Structure

```
.
├── app
│   └── serving_service.py
├── main.py
├── Dockerfile
├── README.md
├── servingservice-pv.yaml
├── servingservice-pvc.yaml
├── servingservice-pod.yaml
├── storage
├────  app
│       └── storage_service.py
│      ├── Dockerfile
│      ├── requirements.txt
│      └── storage_controller.py
└── requirements.txt
```

## License

Licensed under the Apache License, Version 2.0. Copyright 2020-2021 Katana ML, Andrej Baranovskij. [Copy of the license](https://github.com/katanaml/katana-skipper/blob/master/LICENSE).
