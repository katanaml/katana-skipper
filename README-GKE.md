# Katana ML Skipper GKE

Deployment Guide for Google Kubernetes Engine (GKE).

## Author

Katana ML, Andrej Baranovskij

## Instructions

1. Push Skipper images to Docker registry, this registry should be accessible from GKE

2. Open GKE Cloud Shell, follow GKE instructions in Kubernetes setup wizard

![OCI](https://github.com/katanaml/katana-skipper/blob/master/gke-shell.png)

3. Install [NGINX Ingress Controller](https://kubernetes.github.io/ingress-nginx/deploy/#gce-gke) for GKE

4. Clone Skipper repo

```
git clone https://github.com/katanaml/katana-skipper
```

5. Edit rabbitmq/rabbit-statefulset.yaml file, change storageClassName to 'standard-rwo'

```
vim rabbitmq/rabbit-statefulset.yaml
```

6. Edit api/api-ingress.yaml file, remove 'host' element to configure Ingress with GKE public IP

```
vim api/api-ingress.yaml
```

7. There is no need to create Persistent Volume on GKE, it will be provisioned automatically by Volume Claim. Remove this line from kubectl-setup.sh:

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

9. There is no need to create Persistent Volume on GKE, it will be provisioned automatically by Volume Claim. Remove this line from kubectl-setup.sh:

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

11. Training service runs multiple Pods, we must assign all Pod instances to the same Kubernetes node, to make sure all instances can access Persistent Volume. Read more - [Assigning Pods to Nodes](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/)

```
kubectl get nodes
```

```
kubectl label nodes <node-name> skipper=serving
```

```
kubectl get nodes --show-labels
```

12. Add nodeSelector to servingservice-pod.yaml

```
nodeSelector:
    skipper: serving
```

13. Setup Kubernetes services:

```
./kubectl-setup.sh
```

14. Skipper API endpoint URL

```
http://<Load Balancer IP>/api/v1/skipper/tasks/docs
```

Check Load Balancer IP:

![LoadBalancer](https://github.com/katanaml/katana-skipper/blob/master/gke-loadbalancer.png)

## License

Licensed under the Apache License, Version 2.0. Copyright 2020-2021 Katana ML, Andrej Baranovskij. [Copy of the license](https://github.com/katanaml/katana-pipeline/blob/master/LICENSE).
