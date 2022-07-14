<<<<<<< HEAD
#!/bin/bash
ROOT_UID=0
SUCCESS=0
E_USEREXISTS=70
#Run as root
if[ "$UID" -ne "$ROOT_UID" ]
then
    echo "Must be root to run this script"
    exit $E_NOTROOT
fi
# checking if both arguments are there
if [ $# -ne 2 ];then
username=$1
pass=$2
    # Check whether already exists or not
    grep -q "$username" /etc/passwd
    if [ $? -ne 0 ]
    then
        echo "User $username does already exists"
        exit $E_USEREXISTS
    fi
        useradd -p `mkpasswd "$pass"` -d /home/"$username" -m -g users -s /bin/bash "$username"
        echo "The account is setup"
    else
        echo "This programme needs 2 arguments and you have given $#"
fi
=======
#!/bin/bash
ROOT_UID=0
SUCCESS=0
E_USEREXISTS=70
#Run as root
if[ "$UID" -ne "$ROOT_UID" ]
then
    echo "Must be root to run this script"
    exit $E_NOTROOT
fi
# checking if both arguments are there
if [ $# -ne 2 ];then
username=$1
pass=$2
    # Check whether already exists or not
    grep -q "$username" /etc/passwd
    if [ $? -ne 0 ]
    then
        echo "User $username does already exists"
        exit $E_USEREXISTS
    fi
        useradd -p `mkpasswd "$pass"` -d /home/"$username" -m -g users -s /bin/bash "$username"
        echo "The account is setup"
    else
        echo "This programme needs 2 arguments and you have given $#"
fi
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
exit 0