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
                ('category_id', models.IntegerField(default=0, editable=False)),
                ('category_name', models.CharField(editable=False, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(blank=True, max_length=100, null=True)),
                ('max_landing_pad_size', models.CharField(blank=True, max_length=100, null=True)),
                ('distance_to_star', models.BigIntegerField(blank=True, default=0, null=True)),
                ('allegiance', models.CharField(blank=True, max_length=100, null=True)),
                ('government', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('faction', models.CharField(blank=True, max_length=100, null=True)),
                ('has_repair', models.NullBooleanField(default=False)),
                ('has_blackmarket', models.NullBooleanField(default=False)),
                ('has_refuel', models.NullBooleanField(default=False)),
                ('has_rearm', models.NullBooleanField(default=False)),
                ('has_shipyard', models.NullBooleanField(default=False)),
                ('has_outfitting', models.NullBooleanField(default=False)),
                ('has_commodities', models.NullBooleanField(default=False)),
                ('updated_at', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('needs_permit', models.NullBooleanField(default=False)),
                ('primary_economy', models.CharField(max_length=100, null=True)),
                ('population', models.BigIntegerField(default=0, null=True)),
                ('security', models.CharField(max_length=100, null=True)),
                ('allegiance', models.CharField(max_length=100, null=True)),
                ('government', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('faction', models.CharField(max_length=100, null=True)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('z', models.FloatField()),
                ('updated_at', models.BigIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='station',
            name='system',
            field=models.ForeignKey(to='elitedata.System', related_name='stations', editable=False),
        ),
    ]
