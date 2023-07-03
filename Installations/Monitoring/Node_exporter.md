# Install Node Exporter 
## create a system user for Node Exporter

```
sudo useradd --system --no-create-home --shell /bin/false node_exporter
```
## Download Node Exporter

```
https://prometheus.io/download/#node_exporter
```
## Configure Node Exporter
```
tar -xvf node_exporter-1.6.1.linux-amd64.tar.gz
sudo mv node_exporter-1.6.1.linux-amd64/node_exporter /usr/local/bin/
node_exporter --version
sudo vim /etc/systemd/system/node_exporter.service

[Unit]

Description=Node Exporter

Wants=network-online.target

After=network-online.target

 

StartLimitIntervalSec=500

StartLimitBurst=5

 

[Service]

User=node_exporter

Group=node_exporter

Type=simple

Restart=on-failure

RestartSec=5s

ExecStart=/usr/local/bin/node_exporter \

    --collector.logind

 

[Install]

WantedBy=multi-user.target
```

## Start Node Exporter
```
sudo systemctl enable node_exporter
sudo systemctl start node_exporter
sudo systemctl status node_exporter
```
##  Adding static targets to the Prometheus configuration file
```
sudo vim /etc/prometheus/prometheus.yml
- job_name: node_export

    static_configs:

      - targets: ["localhost:9100"]

```
# Check the status 
```
curl -X POST http://localhost:9090/-/reload
```

## we might get life api not enabled ????
```
sudo vim /etc/prometheus/prometheus.yml
- job_name: node_export

    static_configs:

      - targets: ["localhost:9100"]

    metrics_path: /metrics

    scheme: http

```
## Restart Prometheus
```
sudo systemctl restart prometheus.service
```
## Accessing Node port
```
http://<ip>:9100/metrics
```
## Accessing Prometheus Web Interface
```
 http://<ip>:9090/targets
 
```



