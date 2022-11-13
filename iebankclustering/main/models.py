from django.db import models


class IndividualEntrepreneur(models.Model):
    INN = models.BigIntegerField()
    registration_date = models.DateField()
    region = models.TextField()
    okved = models.TextField()
    industry = models.TextField()
    section = models.TextField()

class IECluster(models.Model):
    INN = models.BigIntegerField()
    cluster_id = models.IntegerField(default=-1)
