# Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
from __future__ import unicode_literals

from django.db import models

class EventNames(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)

    class Meta:
        # managed = False
        db_table = 'event_names'


class Events(models.Model):
    id = models.AutoField(primary_key=True)
    investigator = models.ForeignKey('Investigators', models.PROTECT, db_column='investigator')
    date = models.DateField()
    type = models.ForeignKey(EventNames, models.PROTECT, db_column='type')

    class Meta:
        # managed = False
        db_table = 'events'


class Goals(models.Model):
    id = models.AutoField(primary_key=True)
    ward = models.ForeignKey('Wards', models.PROTECT, db_column='ward')
    date = models.DateField()
    type = models.ForeignKey(EventNames, models.PROTECT, db_column='type')
    amount = models.IntegerField()

    class Meta:
        # managed = False
        db_table = 'goals'
