from django.db import models
from django.contrib.auth.models import User
from jsonfield import JSONField

# Create your models here.


class AWSCredentials(models.Model):
    access_key = models.CharField(max_length=128)
    secret_key = models.CharField(max_length=512)
    account_id = models.CharField(max_length=40)
    default_region = models.CharField(max_length=32, default='us-east-1')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.account_id


class EC2(models.Model):
    instance_id = models.CharField(max_length=255, blank=False)
    instance_type = models.CharField(max_length=255, blank=False)
    state = models.BooleanField()
    instance_data = JSONField(null=True)
    credentials = models.ForeignKey(AWSCredentials, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.instance_id} {self.credentials}"
