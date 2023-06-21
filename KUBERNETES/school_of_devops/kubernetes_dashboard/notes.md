# Creating a kubernetes dashboard
mkdir $HOME/certs
cd certs
openssl genrsa -out dashboard.key 2048
openssl rsa -in dashboard.key -out dashboard.key
openssl req -sha256 -new -key dashboard.key -out dashboard.csr
openssl x509 -req -sha256 -days 365 -in dashboard.csr -signkey dashboard.key -out dashboard.crt

# Load the certificate in secret
kubectl create namespace kubernetes-dashboard
kubectl -n kubernetes-dashboard create secret generic kubernetes-dashboard-certs --from-file=$HOME/certs -o yaml

# Deploy the dashboard
kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.0.0-beta8/aio/deploy/recommended.yaml