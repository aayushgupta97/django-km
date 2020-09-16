from .client import Client
from rest_framework import serializers


class TaskCreateSerializer(serializers.Serializer):
    access_key = serializers.CharField(max_length=128)
    secret_key = serializers.CharField(max_length=512)

    def validate(self, attrs):
        """
        :param attrs: Input data from POST request
                  {access_key: <STRING>,
                  secret_key: <STRING>}

        If successfully validated and AWS Credentials are verified, then
        :return: {access_key: <STRING>,
                  secret_key: <STRING>,
                  account_id: <STRING>,
                  }
        """
        aws = Client()
        print(attrs)
        config = dict(
            ak=attrs.get("access_key"),
            sk=attrs.get("secret_key"),
            region=attrs.get("default_region")
        )
        session = aws.session_access_secret_key(config)
        account_id, is_valid = aws.is_valid_credential(session)



        if not is_valid:
            raise serializers.ValidationError("Invalid AWS Credentials.")
        attrs['account_id'] = account_id
        return attrs

