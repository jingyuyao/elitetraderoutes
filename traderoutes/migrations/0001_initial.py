# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('elitedata', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('buy_price', models.IntegerField()),
                ('sell_price', models.IntegerField()),
                ('supply', models.IntegerField()),
                ('demand', models.IntegerField()),
                ('commodity', models.ForeignKey(to='elitedata.Commodity')),
                ('destination_station', models.ForeignKey(to='elitedata.Station', related_name='connection_destination')),
                ('destination_system', models.ForeignKey(to='elitedata.System', related_name='connection_destination')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='route')),
            ],
        ),
        migrations.AddField(
            model_name='connection',
            name='route',
            field=models.ForeignKey(to='traderoutes.Route'),
        ),
        migrations.AddField(
            model_name='connection',
            name='start_station',
            field=models.ForeignKey(to='elitedata.Station', related_name='connection_start'),
        ),
        migrations.AddField(
            model_name='connection',
            name='start_system',
            field=models.ForeignKey(to='elitedata.System', related_name='connection_start'),
        ),
    ]
