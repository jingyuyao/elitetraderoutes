# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elitedata', '0002_auto_20150617_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='stationcommodity',
            name='demand_level',
            field=models.CharField(default='low', max_length=100),
            preserve_default=False,
        ),
    ]
