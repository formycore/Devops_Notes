# Install Grafana on Ubuntu 22.04
```sudo apt-get install -y apt-transport-https
sudo apt-get install -y software-properties-common wget
sudo wget -q -O /usr/share/keyrings/grafana.key https://apt.grafana.com/gpg.key

echo "deb [signed-by=/usr/share/keyrings/grafana.key] https://apt.grafana.com stable main" | sudo tee -a /etc/apt/sources.list.d/grafana.list

echo "deb [signed-by=/usr/share/keyrings/grafana.key] https://apt.grafana.com beta main" | sudo tee -a /etc/apt/sources.list.d/grafana.list

# Updates the list of available packages
sudo apt-get update

# Installs the latest OSS release:
sudo apt-get install grafana


```
# Start Grafana
```
sudo systemctl daemon-reload
sudo systemctl enable grafana-server
sudo systemctl start grafana-server
sudo systemctl status grafana-server
```
## Access Grafana Web Interface
```
http://<ip>:3000
```
# Config Grafana
```
username : admin
password : admin

Select :
        --> Add data source
        --> Prometheus
        --> http://<ip>:9090 # this is prometheus ip
        --> Save & Test
```
# Dashboard
```
---> Click on + icon
--> Import dashboard
--> 1860 # this is dashboard id
--> Load
--> Select Prometheus
--> Import
```

