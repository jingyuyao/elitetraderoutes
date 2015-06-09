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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('buy_price', models.IntegerField(default=0)),
                ('sell_price', models.IntegerField(default=0)),
                ('supply', models.IntegerField(default=0)),
                ('demand', models.IntegerField(default=0)),
                ('commodity', models.ForeignKey(related_name='connections', to='elitedata.Commodity')),
                ('destination_station', models.ForeignKey(related_name='connections_destination', to='elitedata.Station')),
                ('destination_system', models.ForeignKey(related_name='connections_destination', to='elitedata.System')),
                ('owner', models.ForeignKey(related_name='connections', to=settings.AUTH_USER_MODEL, editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(related_name='routes', to=settings.AUTH_USER_MODEL, editable=False)),
            ],
        ),
        migrations.AddField(
            model_name='connection',
            name='route',
            field=models.ForeignKey(related_name='connections', to='traderoutes.Route', editable=False),
        ),
        migrations.AddField(
            model_name='connection',
            name='start_station',
            field=models.ForeignKey(related_name='connections_start', to='elitedata.Station'),
        ),
        migrations.AddField(
            model_name='connection',
            name='start_system',
            field=models.ForeignKey(related_name='connections_start', to='elitedata.System'),
        ),
    ]
