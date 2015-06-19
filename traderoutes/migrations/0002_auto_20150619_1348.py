# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('traderoutes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='connection',
            name='uuid',
            field=models.CharField(auto_created=uuid.uuid4, default=uuid.uuid4, max_length=36),
        ),
        migrations.AddField(
            model_name='route',
            name='uuid',
            field=models.CharField(auto_created=uuid.uuid4, default=uuid.uuid4, max_length=36),
        ),
    ]
