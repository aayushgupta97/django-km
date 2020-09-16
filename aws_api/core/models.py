from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class AWSCredentials(models.Model):
    access_key = models.CharField(max_length=128)
    secret_key = models.CharField(max_length=512)
    account_id = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.access_key


