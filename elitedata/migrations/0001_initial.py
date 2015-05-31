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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(null=True, max_length=100)),
                ('category_id', models.IntegerField(null=True, default=0)),
                ('category_name', models.CharField(null=True, max_length=100)),
                ('average_price', models.IntegerField(null=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('has_repair', models.NullBooleanField(default=False)),
                ('max_landing_pad_size', models.CharField(null=True, max_length=100)),
                ('has_blackmarket', models.NullBooleanField(default=False)),
                ('has_refuel', models.NullBooleanField(default=False)),
                ('has_rearm', models.NullBooleanField(default=False)),
                ('updated_at', models.BigIntegerField()),
                ('government', models.CharField(null=True, max_length=100)),
                ('type', models.CharField(null=True, max_length=100)),
                ('has_commodities', models.NullBooleanField(default=False)),
                ('allegiance', models.CharField(null=True, max_length=100)),
                ('state', models.CharField(null=True, max_length=100)),
                ('has_shipyard', models.NullBooleanField(default=False)),
                ('faction', models.CharField(null=True, max_length=100)),
                ('has_outfitting', models.NullBooleanField(default=False)),
                ('distance_to_star', models.BigIntegerField(null=True, default=0)),
                ('name', models.CharField(null=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('government', models.CharField(null=True, max_length=100)),
                ('needs_permit', models.NullBooleanField(default=False)),
                ('state', models.CharField(null=True, max_length=100)),
                ('security', models.CharField(null=True, max_length=100)),
                ('allegiance', models.CharField(null=True, max_length=100)),
                ('faction', models.CharField(null=True, max_length=100)),
                ('primary_economy', models.CharField(null=True, max_length=100)),
                ('updated_at', models.BigIntegerField()),
                ('population', models.BigIntegerField(null=True, default=0)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('z', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='station',
            name='system',
            field=models.ForeignKey(to='elitedata.System'),
        ),
    ]
