from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    cash = models.IntegerField()
    holdings = JSONField()
