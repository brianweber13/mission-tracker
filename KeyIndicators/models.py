from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class EventPossibility(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    event_possibility_id = models.ForeignKey(EventPossibility, models.PROTECT)
    investigator_id = models.ForeignKey('Investigator', models.PROTECT)
    date = models.DateField()


class Goal(models.Model):
    id = models.AutoField(primary_key=True)
    event_possibility_id = models.ForeignKey(EventPossibility, models.PROTECT)
    amount = models.IntegerField()
    date = models.DateField()
    ward_id = models.ForeignKey('Ward', models.PROTECT)


class Investigator(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    ward_id = models.ForeignKey('Ward', models.PROTECT)
    status = models.CharField(max_length=20, blank=True, null=True)
    baptismal_date = models.DateField(blank=True, null=True)


class Missionary(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=300)
    ward_id = models.ForeignKey('Ward', models.PROTECT)


class Stake(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        combined = str(self.id) + " " + self.name
        return combined


class StatusPossibility(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)


class Ward(models.Model):
    id = models.AutoField(primary_key=True)
    stake_id = models.ForeignKey(Stake, models.PROTECT)
    name = models.CharField(max_length=20)

    def __str__(self):
        combined = str(self.id) + " " + self.name
        # combined = str(self.id) + " " + self.name + ", part of  " + "stake #"
        # combined += str(self.stake_id)
        return combined


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ward_id = models.ForeignKey(Ward, models.PROTECT)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.Profile.save()

