```
sudo chown $USER /var/run/docker.sock
#############################
FROM python:3.9-slim
WORKDIR /app
RUN apt-get update -y \
    && apt-get upgrade -y \
    && apt-get install -y gcc default-libmysqlclient-dev pkg-config \
    && rm -rf /var/lib/apt/list/*
COPY requirements.txt .
RUN pip install mysqlclient
RUN pip install -r requirements.txt
COPY . .
CMD [ "python", "app.py"]
#############################

- docker build -t testnov25:v1 .

# we need another one for the mysql
- docker run -d --name mysql -e MYSQL_ROOT_PASSWORD=123456 mysql:5.7






```