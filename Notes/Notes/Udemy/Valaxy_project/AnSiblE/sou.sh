<<<<<<< HEAD
#!/bin/bash
echo "JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")" | sudo tee -a /etc/profile
=======
#!/bin/bash
echo "JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")" | sudo tee -a /etc/profile
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
source /etc/profile