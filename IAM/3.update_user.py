import boto3

def update_user(olduser, newuser):
    iam = boto3.client('iam')
    response = iam.update_user(UserName=olduser, NewUserName=newuser)
    print(response)
update_user("test_user_1", "update_user1")
