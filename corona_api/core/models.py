from django.db import models


# Create your models here.
class StateWiseData(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=2, unique=True)
    active = models.IntegerField()
    confirmed = models.IntegerField()
    deaths = models.IntegerField()
    recovered = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class CaseTimeSeries(models.Model):
    daily_confirmed = models.IntegerField()
    daily_deceased = models.IntegerField()
    daily_recovered = models.IntegerField()
    total_confirmed = models.IntegerField()
    total_deceased = models.IntegerField()
    total_recovered = models.IntegerField()
    date = models.DateField(unique=True)

    def __str__(self):
        return self.date

