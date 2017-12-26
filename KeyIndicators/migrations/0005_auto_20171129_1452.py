# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 21:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KeyIndicators', '0004_auto_20171129_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_possibility_id',
            new_name='event_possibility',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='investigator_id',
            new_name='investigator',
        ),
        migrations.RenameField(
            model_name='goal',
            old_name='event_possibility_id',
            new_name='event_possibility',
        ),
        migrations.RenameField(
            model_name='goal',
            old_name='ward_id',
            new_name='ward',
        ),
        migrations.RenameField(
            model_name='investigator',
            old_name='ward_id',
            new_name='ward',
        ),
        migrations.RenameField(
            model_name='missionary',
            old_name='ward_id',
            new_name='ward',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='ward_id',
            new_name='ward',
        ),
        migrations.RenameField(
            model_name='ward',
            old_name='stake_id',
            new_name='stake',
        ),
    ]