import boto3

def all_users():
    iam = boto3.client('iam')
    paginator = iam.get_paginator('list_users')
    for response in paginator.paginate():
        for user in response['Users']:
            username = user['UserName']
            Arn = user['Arn']
            print('username : {}  Arn : {}'.format(username, Arn))
all_users()        
    
            
            