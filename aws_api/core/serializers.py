from .client import Client
from rest_framework import serializers

from .models import AWSCredentials


class TaskCreateSerializer(serializers.ModelSerializer):
    def to_internal_value(self, attrs):
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
            raise serializers.ValidationError({"message": "Invalid AWS Credentials."})
        if AWSCredentials.objects.filter(account_id=account_id, user_id=attrs.get("user_id")).exists():
            raise serializers.ValidationError({"message": "This account ID already exists."})

        attrs['account_id'] = account_id
        return attrs

    class Meta:
        model = AWSCredentials
        fields = "__all__"
