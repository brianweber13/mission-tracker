# Generated by Django 2.0.2 on 2018-03-09 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KeyIndicators', '0006_auto_20171129_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investigator',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='KeyIndicators.StatusPossibility'),
        ),
    ]