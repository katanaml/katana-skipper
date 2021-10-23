# Katana ML Skipper GCP

Deployment Guide for Google Cloud Platform (GCP).

## Author

Katana ML, Andrej Baranovskij

## Instructions

1. Push Skipper images to Docker registry, this registry should be accessible from OCI

2. Open OCI Cloud Shell, follow OCI instructions in Kubernetes setup wizard

![OCI](https://github.com/katanaml/katana-skipper/blob/master/oci-shell.png)

3. Install [NGINX Ingress Controller](https://kubernetes.github.io/ingress-nginx/deploy/#oracle-cloud-infrastructure) for OCI

4. Clone Skipper repo

```
git clone https://github.com/katanaml/katana-skipper
```

5. Edit rabbitmq/rabbit-statefulset.yaml file, change storageClassName to 'oci'

```
nano rabbitmq/rabbit-statefulset.yaml
```

6. Edit api/api-ingress.yaml file, remove 'host' element to configure Ingress with OCI public IP

```
nano api/api-ingress.yaml
```

7. Edit services/trainingservice/trainingservice-pv.yaml, change storageClassName to 'oci'

```
nano services/trainingservice/trainingservice-pv.yaml
```

8. Edit services/trainingservice/trainingservice-pvc.yaml, change storageClassName to 'oci'

```
nano services/trainingservice/trainingservice-pvc.yaml
```

9. Edit services/servingservice/servingservice-pv.yaml, change storageClassName to 'oci'

```
nano services/servingservice/servingservice-pv.yaml
```

10. Edit services/servingservice/servingservice-pvc.yaml, change storageClassName to 'oci'

```
nano services/servingservice/servingservice-pvc.yaml
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

![LoadBalancer](https://github.com/katanaml/katana-skipper/blob/master/oci-loadbalancer.png)

13. More info about Kubernetes cluster management on [OCI](https://docs.oracle.com/en/learn/container_engine_kubernetes/#introduction)

## License

Licensed under the Apache License, Version 2.0. Copyright 2020-2021 Katana ML, Andrej Baranovskij. [Copy of the license](https://github.com/katanaml/katana-pipeline/blob/master/LICENSE).
