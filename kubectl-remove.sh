kubectl delete all --all -n katana-skipper

kubectl delete all --all -n rabbits

kubectl delete all --all -n ingress-nginx

kubectl delete -n katana-skipper -f api/api-ingress.yaml

kubectl delete -f services/trainingservice/trainingservice-pv.yaml

kubectl delete -f services/servingservice/servingservice-pv.yaml
