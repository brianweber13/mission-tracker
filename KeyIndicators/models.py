# Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
from __future__ import unicode_literals

from django.db import models

class EventPossibility(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)

    class Meta:
        # managed = False
        db_table = 'event_possibility'


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    event_possibility_id = models.ForeignKey(EventPossibility, models.PROTECT)
    investigator_id = models.ForeignKey('Investigator', models.PROTECT)
    date = models.DateField()

    class Meta:
        # managed = False
        db_table = 'event'


class Goal(models.Model):
    id = models.AutoField(primary_key=True)
    event_possibility_id = models.ForeignKey(EventPossibility, models.PROTECT)
    amount = models.IntegerField()
    date = models.DateField()
    ward_id = models.ForeignKey('Ward', models.PROTECT)

    class Meta:
        # managed = False
        db_table = 'goal'


class Investigator(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    ward_id = models.ForeignKey('Ward', models.PROTECT)
    status = models.CharField(max_length=20, blank=True, null=True)
    baptismal_date = models.DateField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'investigator'


class Missionary(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=300)
    ward_id = models.ForeignKey('Ward', models.PROTECT)

    class Meta:
        # managed = False
        db_table = 'missionary'


class Stake(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    class Meta:
        # managed = False
        db_table = 'stake'

    def __str__(self):
        combined = str(self.id) + " " + self.name
        return combined

class StatusPossibility(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)

    class Meta:
        # managed = False
        db_table = 'status_possibility'


class Ward(models.Model):
    id = models.AutoField(primary_key=True)
    stake_id = models.ForeignKey(Stake, models.PROTECT)
    name = models.CharField(max_length=20)

    class Meta:
        # managed = False
        db_table = 'ward'

    def __str__(self):
        combined = str(self.id) + " " + self.name + " " + "Stake #"
        combined += str(self.stake_id)
        # use triple quotes here?
        return combined

