# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elitedata', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commodity',
            name='created',
        ),
        migrations.RemoveField(
            model_name='station',
            name='created',
        ),
        migrations.RemoveField(
            model_name='system',
            name='created',
        ),
    ]
