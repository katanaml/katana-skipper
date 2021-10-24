# Katana ML Skipper GCP

Deployment Guide for Google Cloud Platform (GCP).

## Author

Katana ML, Andrej Baranovskij

## Instructions

1. Push Skipper images to Docker registry, this registry should be accessible from GCP

2. Open GCP Cloud Shell, follow GCP instructions in Kubernetes setup wizard

![OCI](https://github.com/katanaml/katana-skipper/blob/master/gcp-shell.png)

3. Install [NGINX Ingress Controller](https://kubernetes.github.io/ingress-nginx/deploy/#gce-gke) for GCP

4. Clone Skipper repo

```
git clone https://github.com/katanaml/katana-skipper
```

5. Edit rabbitmq/rabbit-statefulset.yaml file, change storageClassName to 'standard-rwo'

```
vim rabbitmq/rabbit-statefulset.yaml
```

6. Edit api/api-ingress.yaml file, remove 'host' element to configure Ingress with GCP public IP

```
vim api/api-ingress.yaml
```

7. There is no need to create Persistent Volume on GCP, it will be provisioned automatically by Volume Claim. Remove this line from kubectl-setup.sh:

```
kubectl apply -f services/trainingservice/trainingservice-pv.yaml
```

8. Edit services/trainingservice/trainingservice-pvc.yaml, change it to support dynamic provisioning for Persistent Volume, remove storageClassName

```
vim services/trainingservice/trainingservice-pvc.yaml
```

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: training-service-claim
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 500Mi
```

9. There is no need to create Persistent Volume on GCP, it will be provisioned automatically by Volume Claim. Remove this line from kubectl-setup.sh:

```
kubectl apply -f services/servingservice/servingservice-pv.yaml
```

10. Edit services/servingservice/servingservice-pvc.yaml, change it to support dynamic provisioning for Persistent Volume, remove storageClassName

```
vim services/servingservice/servingservice-pvc.yaml
```

```
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: serving-service-claim
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 500Mi
```

11. Setup Kubernetes services:

```
./kubectl-setup.sh
```

12. Skipper API endpoint URL

```
http://<Load Balancer IP>/api/v1/skipper/tasks/docs
```

Check Load Balancer IP:

![LoadBalancer](https://github.com/katanaml/katana-skipper/blob/master/gcp-loadbalancer.png)

## License

Licensed under the Apache License, Version 2.0. Copyright 2020-2021 Katana ML, Andrej Baranovskij. [Copy of the license](https://github.com/katanaml/katana-pipeline/blob/master/LICENSE).
