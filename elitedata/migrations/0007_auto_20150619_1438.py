# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('elitedata', '0006_auto_20150619_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commodity',
            name='uuid',
            field=models.UUIDField(auto_created=uuid.uuid4, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='station',
            name='uuid',
            field=models.UUIDField(auto_created=uuid.uuid4, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='stationcommodity',
            name='uuid',
            field=models.UUIDField(auto_created=uuid.uuid4, default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='system',
            name='uuid',
            field=models.UUIDField(auto_created=uuid.uuid4, default=uuid.uuid4),
        ),
    ]
