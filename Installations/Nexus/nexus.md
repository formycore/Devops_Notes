# Install docker and docker compose
```
version: "3"
services:
  nexus:
    image: sonatype/nexus3
    restart: always
    volumes:
      - "nexus-data:/sonatype-work"
    ports:
      - "8081:8081"
volumes:
  nexus-data: {}
  ```
  