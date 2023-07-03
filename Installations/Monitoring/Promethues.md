# Install Prometheus
sudo useradd --no-create-home --shell /bin/false prometheus

# Step 1 - Update System Packages
```
sudo apt update
```
# Step 2 - Create a System User for Prometheus
```
sudo groupadd --system prometheus
sudo useradd -s /sbin/nologin --system -g prometheus prometheus 
```
# Step 3 - Create Directories for Prometheus
```
sudo mkdir /etc/prometheus
sudo mkdir /var/lib/prometheus
```
# Step 4 - Download Prometheus
```
https://prometheus.io/download/
# here we get on tar file
tar -xvf prometheus-2.2.1.linux-amd64.tar.gz
cd prometheus-2.2.1.linux-amd64

```
# Configuring Prometheus on Ubuntu 22.04
## Step 1 - Move the Binary Files & Set Owner
```
sudo mv prometheus /usr/local/bin
sudo mv promtool /usr/local/bin
sudo chown prometheus:prometheus /usr/local/bin/prometheus
sudo chown prometheus:prometheus /usr/local/bin/promtool
```
## Step 2 - Move the Configuration Files & Set Owner
```
sudo mv consoles /etc/prometheus
sudo mv console_libraries /etc/prometheus
sudo mv prometheus.yml /etc/prometheus

sudo chown prometheus:prometheus /etc/prometheus
sudo chown -R prometheus:prometheus /etc/prometheus/consoles
sudo chown -R prometheus:prometheus /etc/prometheus/console_libraries
sudo chown -R prometheus:prometheus /var/lib/prometheus
```
## Step 3 - Configure Prometheus Service
```
sudo nano /etc/systemd/system/prometheus.service

[Unit]
Description=Prometheus
Wants=network-online.target
After=network-online.target

[Service]
User=prometheus
Group=prometheus
Type=simple
ExecStart=/usr/local/bin/prometheus \
    --config.file /etc/prometheus/prometheus.yml \
    --storage.tsdb.path /var/lib/prometheus/ \
    --web.console.templates=/etc/prometheus/consoles \
    --web.console.libraries=/etc/prometheus/console_libraries

[Install]
WantedBy=multi-user.target
```
## Step 4 - Start Prometheus Service
```
sudo systemctl daemon-reload
sudo systemctl enable prometheus
sudo systemctl start prometheus
sudo systemctl status prometheus
```
## Access Prometheus Web Interface
```
 <ip_address>:9090
```
