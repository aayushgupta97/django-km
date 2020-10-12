from celery import shared_task
from .client import Client
from .models import EC2, AWSCredentials


@shared_task
def task_fetch_ec2_data(credential_id):
    """
    Periodically update EC2 for the Resource provided.
    :param credential_id:
    :return:
    """
    cred = AWSCredentials.objects.get(credential_id)
    aws = Client()
    config = dict(
        ak=cred.access_key,
        sk=cred.secret_key,
        region=cred.default_region
    )
    session = aws.session_access_secret_key(config)
    account_id, is_valid = aws.is_valid_credential(session)
    if is_valid:
        client = session.client('ec2')
        pager = client.get_paginator('describe_instances')

        for page in pager.paginate():
            if page['ResponseMetadata']['HTTPStatusCode'] == 200:
                for r in (page["Reservations"]):
                    for i in r['Instances']:
                        if i['State']['Name'] == 'running':
                            state = True
                        elif i['State']['Name'] == 'stopped':
                            state = False
                        else:
                            state = False

                        EC2.objects.update_or_create(credentials=cred,
                                                     instance_id=['InstanceId'],
                                                     defaults={
                                                         "instance_type": i['InstanceType'],
                                                         "state": state,
                                                         "instance_data": i
                                                     })
                return True
            return False




