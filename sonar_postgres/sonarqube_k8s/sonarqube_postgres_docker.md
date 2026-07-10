# PostgreSQL on EC2 + SonarQube on Docker (Complete DevOps Deployment Guide)

## Objective

Deploy PostgreSQL on EC2 Server-1 and SonarQube in Docker on EC2
Server-2 using private networking.

## Architecture

``` text
                 AWS VPC

+---------------------------+      TCP/5432      +-----------------------------+
| EC2-1                     |<------------------>| EC2-2                       |
| PostgreSQL 18             |                    | Docker Engine               |
| PostgreSQL Server: 172.31.15.162 |               | Docker/SonarQube Server: 172.31.8.100 |
| Port 5432                 |                    | Port 9000                  |
+---------------------------+                    +-----------------------------+
                                                        |
                                                        |
                                                Browser :9000
```

# Phase 1 - Prepare EC2

## Server1

-   Ubuntu 24.04
-   PostgreSQL 18

## Server2

-   Ubuntu 24.04
-   Docker
-   PostgreSQL Client

Both servers must be in the same VPC.

------------------------------------------------------------------------

# Phase 2 - Configure Security Groups

PostgreSQL Server - SSH 22 from Admin IP - TCP 5432 from SonarQube EC2
Security Group

SonarQube Server - SSH 22 - TCP 9000 from Internet - Outbound All

------------------------------------------------------------------------

# Phase 3 - Install PostgreSQL

``` bash
sudo apt update
sudo apt upgrade -y
sudo apt install postgresql postgresql-contrib -y
sudo systemctl enable postgresql
sudo systemctl start postgresql
sudo systemctl status postgresql
```

Verify version

``` bash
psql --version
```

------------------------------------------------------------------------

# Phase 4 - Configure Database

``` bash
sudo -i -u postgres
psql
```

``` sql
CREATE DATABASE sonarqube;
CREATE USER sonar WITH ENCRYPTED PASSWORD 'StrongPassword@123';
GRANT ALL PRIVILEGES ON DATABASE sonarqube TO sonar;
```
## Issue 4

Error

permission denied for schema public

Root Cause

Database privilege and schema privilege are different.

Fix

Run the following on the PostgreSQL server at 172.31.15.162 as the postgres user:

``` sql
ALTER DATABASE sonarqube OWNER TO sonar;
ALTER SCHEMA public OWNER TO sonar;
GRANT ALL ON SCHEMA public TO sonar;
GRANT CREATE ON SCHEMA public TO sonar;
```

Exit.

------------------------------------------------------------------------

# Phase 5 - Configure PostgreSQL

Paths on Ubuntu (adjust the version number if your PostgreSQL installation is not 18):

- postgresql.conf: /etc/postgresql/18/main/postgresql.conf
- pg_hba.conf: /etc/postgresql/18/main/pg_hba.conf

Edit postgresql.conf

``` conf
listen_addresses='*'
```

Edit pg_hba.conf

``` conf
host sonarqube sonar 172.31.8.100/32 md5
```

Restart

``` bash
sudo systemctl restart postgresql
```

Verify

``` bash
sudo ss -tlnp | grep 5432
```

Expected

    0.0.0.0:5432

------------------------------------------------------------------------

# Phase 6 - Install PostgreSQL Client on SonarQube Server

``` bash
sudo apt update
sudo apt install postgresql-client -y
```

Connectivity test

Run this from the Docker/SonarQube server at 172.31.8.100:

``` bash
psql -h 172.31.15.162 -U sonar -d sonarqube
```

This should succeed before installing SonarQube.

------------------------------------------------------------------------

# Phase 7 - Install Docker

``` bash
sudo apt update
sudo apt install docker.io -y
sudo systemctl enable docker
sudo systemctl start docker
docker --version
```

------------------------------------------------------------------------

# Phase 8 - Deploy SonarQube

``` bash
docker run -d --name sonarqube -p 9000:9000 -e SONAR_JDBC_URL=jdbc:postgresql://172.31.15.162:5432/sonarqube -e SONAR_JDBC_USERNAME=sonar -e SONAR_JDBC_PASSWORD='StrongPassword@123' sonarqube:26.7.0.124771-community
```

------------------------------------------------------------------------

# Troubleshooting Journey

## Issue 1

Error: Connection refused

Root Cause: Wrong JDBC IP address.

Fix: Updated JDBC URL to PostgreSQL private IP (172.31.15.162).

------------------------------------------------------------------------

## Issue 2

Used

SONAR_JDBC_USER

Root Cause: Incorrect environment variable.

Fix

SONAR_JDBC_USERNAME

------------------------------------------------------------------------

## Issue 3

Database authentication failed.

Root Cause: Username variable was incorrect.

Fix: Corrected environment variable and restarted container.

------------------------------------------------------------------------



------------------------------------------------------------------------

## Issue 5

Needed to verify PostgreSQL networking.

Commands

``` bash
sudo ss -tlnp | grep 5432
hostname -I
```

Confirmed PostgreSQL listening on all interfaces.

------------------------------------------------------------------------

# Validation Checklist

-   PostgreSQL installed
-   Database created
-   User created
-   listen_addresses='\*'
-   pg_hba.conf updated
-   Security Groups configured
-   PostgreSQL Client connectivity tested
-   Docker installed
-   SonarQube deployed
-   JDBC connection successful
-   Schema permissions fixed

------------------------------------------------------------------------

# Best Practices

-   Use private IPs only.
-   Never expose PostgreSQL publicly.
-   Use Docker volumes for SonarQube data.
-   Store passwords in Secrets Manager or Docker secrets.
-   Backup PostgreSQL regularly.
-   Monitor PostgreSQL and SonarQube.
-   Use Nginx + HTTPS for production.
-   Validate connectivity with psql before starting applications.

------------------------------------------------------------------------

# Lessons Learned

1.  Verify network before application.
2.  Read logs sequentially.
3.  Validate environment variable names carefully.
4.  Database ownership does not imply schema ownership.
5.  Test every layer independently (Network → DB → Client →
    Application).
