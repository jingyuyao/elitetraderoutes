# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('elitedata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('buy_price', models.IntegerField(default=0)),
                ('sell_price', models.IntegerField(default=0)),
                ('supply', models.IntegerField(default=0)),
                ('demand', models.IntegerField(default=0)),
                ('commodity', models.ForeignKey(to='elitedata.Commodity', related_name='connections')),
                ('destination_station', models.ForeignKey(to='elitedata.Station', related_name='connections_destination')),
                ('destination_system', models.ForeignKey(to='elitedata.System', related_name='connections_destination')),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='connections', editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='routes', editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='connection',
            name='route',
            field=models.ForeignKey(to='traderoutes.Route', related_name='connections', editable=False),
        ),
        migrations.AddField(
            model_name='connection',
            name='start_station',
            field=models.ForeignKey(to='elitedata.Station', related_name='connections_start'),
        ),
        migrations.AddField(
            model_name='connection',
            name='start_system',
            field=models.ForeignKey(to='elitedata.System', related_name='connections_start'),
        ),
    ]
