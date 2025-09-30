# SonarQube HTTPS Setup on AWS EC2 with Docker

## Overview

This guide shows how to run SonarQube on an AWS EC2 instance using Docker, and access it via HTTPS **without a domain** (using a self-signed certificate). SonarQube runs on HTTP internally (port 9000), and Nginx acts as a reverse proxy for HTTPS.

---

## Directory Structure

```
/home/ubuntu/nginx/
├── certs/           # selfsigned.crt + selfsigned.key
├── conf.d/          # nginx config directory (optional, for multiple configs)
├── default.conf     # main nginx config file
```

---

## Step 1: Generate a Self-Signed Certificate

Replace `<EC2_PUBLIC_IP>` with your instance's public IP.

```bash
mkdir -p ~/nginx/certs
openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout ~/nginx/certs/selfsigned.key \
  -out ~/nginx/certs/selfsigned.crt \
  -subj "/CN=<EC2_PUBLIC_IP>"
```

---

## Step 2: Create Nginx Config

Create `~/nginx/default.conf` with:

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

---

## Step 3: Run SonarQube Container

```bash
docker run -d \
  --name sonarqube \
  -p 9000:9000 \
  -v sonarqube_data:/opt/sonarqube/data \
  sonarqube:lts-community
```

---

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

---

## Step 5: AWS Security Group

- Allow inbound traffic on ports **80** and **443** from `0.0.0.0/0`.

---

## Step 6: Verification

- Check Nginx config inside container:

  ```bash
  docker exec -it nginx cat /etc/nginx/conf.d/default.conf
  ```

- Check Nginx is listening:

  ```bash
  docker exec -it nginx netstat -tulpn
  ```

- Test locally on EC2:

  ```bash
  curl -vk https://localhost
  ```

- Access from browser:

  ```
  https://<EC2_PUBLIC_IP>/
  ```

  > Note: You will see a browser warning due to the self-signed certificate.

---

## Troubleshooting

- If Nginx is not listening, check logs:

  ```bash
  docker logs nginx
  ```

- If config is not mounted, recreate `default.conf` as a file (not a directory).
- Ensure security group rules are correct.
- Use the container name (`sonarqube`) in `proxy_pass`, **not** the EC2 public IP.

---

## Prompt for Reproduction

> I want to run SonarQube on an AWS EC2 instance using Docker and access it via HTTPS. I don’t have a domain, so I want to use a self-signed certificate. SonarQube should run on its default HTTP port internally (9000), and Nginx should act as a reverse proxy handling HTTPS. The EC2 instance should allow external access through ports 80 and 443. I want a clean setup using proper Docker mounts and a directory structure like:
>
> /home/ubuntu/nginx/
> ├── certs/           # selfsigned.crt + selfsigned.key
> ├── conf.d/          # nginx config directory
> ├── default.conf     # main nginx config file
>
> Requirements:
>
> - Nginx should forward requests from HTTPS to the SonarQube container using the container name (sonarqube) instead of the EC2 public IP.
> - Provide the commands to generate a self-signed certificate for the EC2 public IP.
> - Provide proper docker run commands for SonarQube and Nginx.
> - Ensure that the setup works even if the EC2 public IP changes (no domain needed).
> - Include instructions for verifying Nginx and SonarQube are running correctly and listening


https://chatgpt.com/share/68db8443-00a4-8007-b638-a9354e095086