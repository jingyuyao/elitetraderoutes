# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('average_price', models.IntegerField(blank=True, default=0, null=True)),
                ('category_id', models.IntegerField(editable=False, default=0)),
                ('category_name', models.CharField(editable=False, max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(blank=True, null=True, max_length=100)),
                ('max_landing_pad_size', models.CharField(blank=True, null=True, max_length=100)),
                ('distance_to_star', models.BigIntegerField(blank=True, default=0, null=True)),
                ('allegiance', models.CharField(blank=True, null=True, max_length=100)),
                ('government', models.CharField(blank=True, null=True, max_length=100)),
                ('state', models.CharField(blank=True, null=True, max_length=100)),
                ('faction', models.CharField(blank=True, null=True, max_length=100)),
                ('has_repair', models.NullBooleanField(default=False)),
                ('has_blackmarket', models.NullBooleanField(default=False)),
                ('has_refuel', models.NullBooleanField(default=False)),
                ('has_rearm', models.NullBooleanField(default=False)),
                ('has_shipyard', models.NullBooleanField(default=False)),
                ('has_outfitting', models.NullBooleanField(default=False)),
                ('has_commodities', models.NullBooleanField(default=False)),
                ('updated_at', models.BigIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StationCommodity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('buy_price', models.IntegerField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('sell_price', models.IntegerField(default=0)),
                ('demand', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('commodity', models.ForeignKey(editable=False, to='elitedata.Commodity', related_name='station_commodities')),
                ('station', models.ForeignKey(editable=False, to='elitedata.Station', related_name='station_commodities')),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('needs_permit', models.NullBooleanField(default=False)),
                ('primary_economy', models.CharField(null=True, max_length=100)),
                ('population', models.BigIntegerField(default=0, null=True)),
                ('security', models.CharField(null=True, max_length=100)),
                ('allegiance', models.CharField(null=True, max_length=100)),
                ('government', models.CharField(null=True, max_length=100)),
                ('state', models.CharField(null=True, max_length=100)),
                ('faction', models.CharField(null=True, max_length=100)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('z', models.FloatField()),
                ('updated_at', models.BigIntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='station',
            name='system',
            field=models.ForeignKey(editable=False, to='elitedata.System', related_name='stations'),
        ),
    ]
