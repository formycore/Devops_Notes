<<<<<<< HEAD
import boto3

def get_client_object():
    session=boto3.session.Session(profile_name="root")
    iam_client=session.client("iam")


def main():
    iam_client=get_client_object()
    IAM_user_name="lenovo123"
    PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
    iam_client.create_user(UserName=Iam_user_name)
    iam_client.attach_user_policy(UserName=Iam_user_name,PolicyArn=PolicyArn)
    print("AccessKeyId={}\nSecretAccessKey={}".format(response['AccessKey']['AccessKeyId'],response['AccessKey']['SecretAccessKey']))


if __name__=="__main__":
    main()
=======
import boto3

def get_client_object():
    session=boto3.session.Session(profile_name="root")
    iam_client=session.client("iam")


def main():
    iam_client=get_client_object()
    IAM_user_name="lenovo123"
    PolicyArn="arn:aws:iam::aws:policy/AdministratorAccess"
    iam_client.create_user(UserName=Iam_user_name)
    iam_client.attach_user_policy(UserName=Iam_user_name,PolicyArn=PolicyArn)
    print("AccessKeyId={}\nSecretAccessKey={}".format(response['AccessKey']['AccessKeyId'],response['AccessKey']['SecretAccessKey']))


if __name__=="__main__":
    main()
>>>>>>> 9fe199743c6df19ba1530059bc0dd794606c74e5
