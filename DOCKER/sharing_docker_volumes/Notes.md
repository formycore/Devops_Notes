container 1 having war file and container 2 having tomcat deploy container 1 war to container 2 tomcat with volume sharing
**********************************************************************************

Sure, here's an example of how you can share a volume between two Docker containers and deploy a WAR file from one container to another.

    First, create a named volume to share between the containers:


```docker volume create my-shared-data```

    Start the Tomcat container with the shared volume mounted:

```docker run -d --name tomcat -v my-shared-data:/usr/local/tomcat/webapps tomcat:latest```

This command will start the Tomcat container with the named volume my-shared-data mounted at /```usr/local/tomcat/webapps```.

    Copy the WAR file to the shared volume:

```docker run --rm -v $(pwd):/src -v my-shared-data:/dest busybox cp /src/myapp.war /dest/```

This command will copy the myapp.war file to the shared volume my-shared-data.

    Start the container with the WAR file and share the same volume:

```docker run -d --name app -v my-shared-data:/data myapp:latest```

This command will start the container with the myapp image, which has the WAR file in it. It also mounts the same volume my-shared-data at /data.

    Deploy the WAR file to Tomcat:


```docker exec -it tomcat bash
cp /usr/local/tomcat/webapps/ROOT/index.html /usr/local/tomcat/webapps/ROOT/index.html.bak
rm -rf /usr/local/tomcat/webapps/ROOT/*
cp /usr/local/tomcat/webapps/myapp.war /usr/local/tomcat/webapps/ROOT.war
cd /usr/local/tomcat/webapps/
unzip -q -d ROOT ROOT.war
rm -f ROOT.war
exit
```
This set of commands will copy the existing index.html file to a backup location, remove the contents of the ROOT directory, copy the myapp.war file to ROOT.war, unzip it to ROOT directory, and remove the WAR file.

After these steps, the myapp application should be deployed to the Tomcat container and accessible at http://<tomcat-container-ip>:8080/myapp.
