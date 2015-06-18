# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elitedata', '0003_stationcommodity_demand_level'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stationcommodity',
            old_name='stock',
            new_name='supply',
        ),
        migrations.AddField(
            model_name='stationcommodity',
            name='supply_level',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='stationcommodity',
            name='demand_level',
            field=models.CharField(null=True, max_length=100, blank=True),
        ),
    ]
