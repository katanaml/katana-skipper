# Katana ML Skipper OCI

Deployment Guide for Oracle Cloud Infrastructure (OCI).

## Author

Katana ML, Andrej Baranovskij

## Instructions

1. Push Skipper images to Docker registry, this registry should be accessible from OCI

2. Open Cloud Shell

3. Clone Skipper repo

4. Edit rabbitmq/rabbit-statefulset.yaml file, change storageClassName to 'oci'

5. Install [NGINX Ingress Controller](https://kubernetes.github.io/ingress-nginx/deploy/#oracle-cloud-infrastructure) for OCI

6. Edit api/api-ingress.yaml file, remove 'host' reference to configure Inrgess with OCI public IP

```
git clone https://github.com/katanaml/katana-skipper
```

## License

Licensed under the Apache License, Version 2.0. Copyright 2020-2021 Katana ML, Andrej Baranovskij. [Copy of the license](https://github.com/katanaml/katana-pipeline/blob/master/LICENSE).
