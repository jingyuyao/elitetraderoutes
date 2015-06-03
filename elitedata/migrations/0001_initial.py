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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('average_price', models.IntegerField(null=True, default=0, blank=True)),
                ('category_id', models.IntegerField(default=0, editable=False)),
                ('category_name', models.CharField(editable=False, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(null=True, max_length=100, blank=True)),
                ('max_landing_pad_size', models.CharField(null=True, max_length=100, blank=True)),
                ('distance_to_star', models.BigIntegerField(default=0)),
                ('allegiance', models.CharField(null=True, max_length=100, blank=True)),
                ('government', models.CharField(null=True, max_length=100, blank=True)),
                ('state', models.CharField(null=True, max_length=100, blank=True)),
                ('faction', models.CharField(null=True, max_length=100, blank=True)),
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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('needs_permit', models.NullBooleanField(default=False)),
                ('primary_economy', models.CharField(null=True, max_length=100)),
                ('population', models.BigIntegerField(null=True, default=0)),
                ('security', models.CharField(null=True, max_length=100)),
                ('allegiance', models.CharField(null=True, max_length=100)),
                ('government', models.CharField(null=True, max_length=100)),
                ('state', models.CharField(null=True, max_length=100)),
                ('faction', models.CharField(null=True, max_length=100)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('z', models.FloatField()),
                ('updated_at', models.BigIntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='station',
            name='system',
            field=models.ForeignKey(editable=False, related_name='stations', to='elitedata.System'),
        ),
    ]
