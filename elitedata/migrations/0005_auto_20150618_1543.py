# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elitedata', '0004_auto_20150618_1523'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stationcommodity',
            options={'ordering': ['-created']},
        ),
    ]
