# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('traderoutes', '0002_auto_20150619_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connection',
            name='uuid',
            field=models.UUIDField(auto_created=uuid.uuid4, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='route',
            name='uuid',
            field=models.UUIDField(auto_created=uuid.uuid4, default=uuid.uuid4),
        ),
    ]
