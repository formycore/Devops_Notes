# SonarQube + Nginx HTTPS Setup on AWS EC2 with Docker

This guide explains how to run SonarQube on an AWS EC2 instance using Docker and access it via HTTPS with a self-signed certificate.

## Directory Structure

```
/home/ubuntu/nginx/
├── certs/           # selfsigned.crt + selfsigned.key
├── conf.d/          # nginx config directory
├── default.conf     # main nginx config file
```

## Step 1: Generate Self-Signed Certificate

```bash
mkdir -p ~/nginx/certs
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout ~/nginx/certs/selfsigned.key \
  -out ~/nginx/certs/selfsigned.crt \
  -subj "/CN=<EC2_PUBLIC_IP>"
```

> Replace `<EC2_PUBLIC_IP>` with your EC2 public IP.

## Step 2: Run SonarQube Container

```bash
docker run -d \
  --name sonarqube \
  -p 9000:9000 \
  -v sonarqube_data:/opt/sonarqube/data \
  sonarqube:lts-community
```

## Step 3: Create Nginx Config

File: `~/nginx/default.conf`

```nginx
server {
    listen 443 ssl;
    server_name _;

    ssl_certificate /etc/nginx/certs/selfsigned.crt;
    ssl_certificate_key /etc/nginx/certs/selfsigned.key;

    location / {
        proxy_pass http://sonarqube:9000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

server {
    listen 80;
    server_name _;
    return 301 https://$host$request_uri;
}
```

## Step 4: Run Nginx Container

```bash
docker rm -f nginx

docker run -d \
  --name nginx \
  -p 80:80 -p 443:443 \
  --link sonarqube:sonarqube \
  -v ~/nginx/certs:/etc/nginx/certs \
  -v ~/nginx/default.conf:/etc/nginx/conf.d/default.conf \
  nginx:alpine
```

## Step 5: Verify Containers

1. Check Nginx config inside container:

```bash
docker exec -it nginx cat /etc/nginx/conf.d/default.conf
```

2. Check if Nginx is listening on ports 80 and 443:

```bash
docker exec -it nginx netstat -tulpn
```

3. Test from EC2:

```bash
curl -vk https://localhost
```

4. Open in browser:

```text
https://<EC2_PUBLIC_IP>/
```

> Browser will warn about self-signed certificate.

## Step 6: Security Group

Make sure your EC2 Security Group allows inbound traffic on:

* Port 80 (HTTP)
* Port 443 (HTTPS)

## Notes

* Always use `proxy_pass http://sonarqube:9000;` inside Nginx to refer to the container name.
* Avoid using the EC2 public IP inside `proxy_pass`.
* Optional: Move multiple Nginx configs into `conf.d/` for easier management.

## References

* [SonarQube Docker Image](https://hub.docker.com/_/sonarqube)
* [Nginx Docker Image](https://hub.docker.com/_/nginx)
