from utils import days_old

def is_key_old(key, threshold=90):
    return days_old(key['CreateDate']) > threshold

def has_admin_policy(policies):
    for policy in policies:
        if 'AdministratorAccess' in policy['PolicyName']:
            return True
    return False
