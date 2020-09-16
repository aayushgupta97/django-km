import boto3
from botocore.exceptions import ClientError


class Client:
    @staticmethod
    def session_access_secret_key(config):
        """
        Creates the AWS session with ACCESS AND SECREY KEY.
        """
        session = boto3.Session(
            aws_access_key_id=config['ak'],
            aws_secret_access_key=config['sk'],
            region_name=config['region']
        )
        return session

    def is_valid_credential(self, session):
        """
        To check if the AWS credentials are valid.
        :returns: type -> tuple
        (account_id, is_valid_flag)
        AWS Account ID, boolean(True) if the Session is successfully created.
        NONE, boolean(False) if the session is not created successfully.
        """
        try:
            account_id = self.get_account_id(session)
            return account_id, True
        except ClientError:
            return None, False

    @staticmethod
    def get_account_id(session):
        account_id = session.client('sts').get_caller_identity().get('Account')
        return account_id
