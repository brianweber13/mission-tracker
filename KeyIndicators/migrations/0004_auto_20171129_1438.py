# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-29 21:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KeyIndicators', '0003_auto_20171129_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_id',
            new_name='user',
        ),
    ]