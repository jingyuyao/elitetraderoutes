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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('buy_price', models.IntegerField()),
                ('sell_price', models.IntegerField()),
                ('supply', models.IntegerField()),
                ('demand', models.IntegerField()),
                ('commodity', models.ForeignKey(related_name='connections', to='elitedata.Commodity')),
                ('destination_station', models.ForeignKey(related_name='connections_destination', to='elitedata.Station')),
                ('destination_system', models.ForeignKey(related_name='connections_destination', to='elitedata.System')),
                ('owner', models.ForeignKey(related_name='connections', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(related_name='routes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='connection',
            name='route',
            field=models.ForeignKey(related_name='connections', to='traderoutes.Route'),
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
