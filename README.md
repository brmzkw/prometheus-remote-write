# What is

Infrastructure example of prometheus + prometheus remote write + grafana to add monitoring of a simple Python application.

# Instructions

Run `make` to start four containers:

* `prometheus` to store metrics
* `grafana`
* `prometheus-writer` which reads data exposed by `my-hypervisor` and remote writes to `prometheus`
* `my-hypervisor`, a simple Python app exposing metrics

To create a dashboard in grafana, go to http://localhost:9091 configure a Prometheus datasource with url `http://prometheus:9090`.
