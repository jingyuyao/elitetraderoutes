from django.db import models

# Create your models here.

class System(models.Model):
    name = models.CharField(max_length=100)
    government = models.CharField(max_length=100, null=True)
    needs_permit = models.NullBooleanField(default=False)
    state = models.CharField(max_length=100, null=True)
    security = models.CharField(max_length=100, null=True)
    allegiance = models.CharField(max_length=100, null=True)
    faction = models.CharField(max_length=100, null=True)
    primary_economy = models.CharField(max_length=100, null=True)
    updated_at = models.BigIntegerField()
    population = models.BigIntegerField(default=0, null=True)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()


class Station(models.Model):
    has_repair = models.NullBooleanField(default=False)
    max_landing_pad_size = models.CharField(max_length=100, null=True)  # L or M
    has_blackmarket = models.NullBooleanField(default=False)
    has_refuel = models.NullBooleanField(default=False)
    has_rearm = models.NullBooleanField(default=False)
    updated_at = models.BigIntegerField()
    government = models.CharField(max_length=100, null=True)
    type = models.CharField(max_length=100, null=True)
    has_commodities = models.NullBooleanField(default=False)
    allegiance = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    has_shipyard = models.NullBooleanField(default=False)
    faction = models.CharField(max_length=100, null=True)
    has_outfitting = models.NullBooleanField(default=False)
    distance_to_star = models.BigIntegerField(default=0, null=True)
    name = models.CharField(max_length=100, null=True)
    system = models.ForeignKey(System)


class Commodity(models.Model):
    name = models.CharField(max_length=100, null=True)
    category_id = models.IntegerField(default=0, null=True)
    category_name = models.CharField(max_length=100, null=True)
    average_price = models.IntegerField(default=0, null=True)