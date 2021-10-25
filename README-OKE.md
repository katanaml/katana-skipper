# Katana ML Skipper OKE

Deployment Guide for Oracle Cloud Infrastructure (OKE).

## Author

Katana ML, Andrej Baranovskij

## Instructions

1. Push Skipper images to Docker registry, this registry should be accessible from OKE

2. Open OKE Cloud Shell, follow OKE instructions in Kubernetes setup wizard

![OKE](https://github.com/katanaml/katana-skipper/blob/master/oke-shell.png)

3. Install [NGINX Ingress Controller](https://kubernetes.github.io/ingress-nginx/deploy/#oracle-cloud-infrastructure) for OKE

4. Clone Skipper repo

```
git clone https://github.com/katanaml/katana-skipper
```

5. Edit rabbitmq/rabbit-statefulset.yaml file, change storageClassName to 'oci'

```
nano rabbitmq/rabbit-statefulset.yaml
```

6. Edit api/api-ingress.yaml file, remove 'host' element to configure Ingress with OKE public IP

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

![LoadBalancer](https://github.com/katanaml/katana-skipper/blob/master/oke-loadbalancer.png)

13. More info about Kubernetes cluster management on [OKE](https://docs.oracle.com/en/learn/container_engine_kubernetes/#introduction)

## License

Licensed under the Apache License, Version 2.0. Copyright 2020-2021 Katana ML, Andrej Baranovskij. [Copy of the license](https://github.com/katanaml/katana-pipeline/blob/master/LICENSE).
