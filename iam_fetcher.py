import boto3

iam = boto3.client('iam')

def get_iam_users():
    return iam.list_users()['Users']

def get_user_policies(username):
    return iam.list_attached_user_policies(UserName=username)['AttachedPolicies']

def get_inline_policies(username):
    return iam.list_user_policies(UserName=username)['PolicyNames']

def get_access_keys(username):
    return iam.list_access_keys(UserName=username)['AccessKeyMetadata']
