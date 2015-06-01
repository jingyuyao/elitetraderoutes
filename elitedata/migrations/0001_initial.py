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
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('category_id', models.IntegerField(null=True, default=0)),
                ('category_name', models.CharField(max_length=100, null=True)),
                ('average_price', models.IntegerField(null=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('has_repair', models.NullBooleanField(default=False)),
                ('max_landing_pad_size', models.CharField(max_length=100, null=True)),
                ('has_blackmarket', models.NullBooleanField(default=False)),
                ('has_refuel', models.NullBooleanField(default=False)),
                ('has_rearm', models.NullBooleanField(default=False)),
                ('updated_at', models.BigIntegerField()),
                ('government', models.CharField(max_length=100, null=True)),
                ('type', models.CharField(max_length=100, null=True)),
                ('has_commodities', models.NullBooleanField(default=False)),
                ('allegiance', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('has_shipyard', models.NullBooleanField(default=False)),
                ('faction', models.CharField(max_length=100, null=True)),
                ('has_outfitting', models.NullBooleanField(default=False)),
                ('distance_to_star', models.BigIntegerField(null=True, default=0)),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('government', models.CharField(max_length=100, null=True)),
                ('needs_permit', models.NullBooleanField(default=False)),
                ('state', models.CharField(max_length=100, null=True)),
                ('security', models.CharField(max_length=100, null=True)),
                ('allegiance', models.CharField(max_length=100, null=True)),
                ('faction', models.CharField(max_length=100, null=True)),
                ('primary_economy', models.CharField(max_length=100, null=True)),
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
