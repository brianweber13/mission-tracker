# Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
from __future__ import unicode_literals

from django.db import models

class Stakes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        # managed = False
        db_table = 'stakes'


class Wards(models.Model):
    id = models.AutoField(primary_key=True)
    stake_key = models.ForeignKey(Stakes, models.PROTECT, db_column='stake_key')
    name = models.CharField(max_length=20)

    class Meta:
        # managed = False
        db_table = 'wards'
