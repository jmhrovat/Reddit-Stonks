from django.db import models
from django.contrib.postgres.fields import JSONField


# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    cash = models.IntegerField()
    holdings = JSONField(default=dict)
