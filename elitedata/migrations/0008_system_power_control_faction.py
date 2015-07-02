# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elitedata', '0007_auto_20150619_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='system',
            name='power_control_faction',
            field=models.CharField(null=True, max_length=100),
        ),
    ]
