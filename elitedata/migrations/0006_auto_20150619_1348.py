# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('elitedata', '0005_auto_20150618_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='commodity',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, max_length=36, auto_created=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='station',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, max_length=36, auto_created=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='stationcommodity',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, max_length=36, auto_created=uuid.uuid4),
        ),
        migrations.AddField(
            model_name='system',
            name='uuid',
            field=models.CharField(default=uuid.uuid4, max_length=36, auto_created=uuid.uuid4),
        ),
    ]
