from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class EventPossibility(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return str(self.id) + ' ' + self.name


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    event_possibility = models.ForeignKey(EventPossibility, models.PROTECT)
    investigator = models.ForeignKey('Investigator', models.PROTECT)
    date = models.DateField()

    def __str__(self):
        combined = str(self.id) + ' investigator: '
        combined += self.investigator.first_name + ' '
        combined += self.investigator.last_name + ', event: '
        combined += self.event_possibility.name + ', date: '
        combined += self.date


class Goal(models.Model):
    id = models.AutoField(primary_key=True)
    event_possibility = models.ForeignKey(EventPossibility, models.PROTECT)
    amount = models.IntegerField()
    date = models.DateField()
    ward = models.ForeignKey('Ward', models.PROTECT)


class Investigator(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    ward = models.ForeignKey('Ward', models.PROTECT)
    status = models.CharField(max_length=20, blank=True, null=True)
    baptismal_date = models.DateField(blank=True, null=True)


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
    stake = models.ForeignKey(Stake, models.PROTECT)
    name = models.CharField(max_length=20)

    def __str__(self):
        combined = str(self.id) + " " + self.name
        # combined = str(self.id) + " " + self.name + ", part of  " + "stake #"
        # combined += str(self.stake)
        return combined


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ward = models.ForeignKey(Ward, models.PROTECT)

    def __str__(self):
        return "username: " + self.user.username + ", ward: " + self.ward.name

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
# 
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()

