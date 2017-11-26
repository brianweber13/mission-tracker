# Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
from __future__ import unicode_literals

from django.db import models

class Investigators(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    ward = models.ForeignKey('Wards', models.PROTECT, db_column='ward')
    status = models.CharField(max_length=20, blank=True, null=True)
    baptismal_date = models.DateField()

    class Meta:
        # managed = False
        db_table = 'investigators'


class Missionaries(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=300)
    ward = models.ForeignKey('Wards', models.PROTECT, db_column='ward')

    class Meta:
        # managed = False
        db_table = 'missionaries'

