# How ot run MongoDb in your minikube cluster

```shell
helm install mongodb bitnami/mongodb -f values.yaml
minikube tunnel # Open ports to the local enveironment
```
