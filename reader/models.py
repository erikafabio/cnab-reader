from django.db import models


class FileModel(models.Model):
    type_of_transition = models.CharField(max_length=1)
    date = models.CharField(max_length=16)
    value = models.FloatField()
    cpf = models.IntegerField()
    card = models.CharField(max_length=12)
    hour = models.TimeField()
    market_owner = models.CharField(max_length=14)
    market_name = models.CharField(max_length=19)