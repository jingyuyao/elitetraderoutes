from django.db import models

# Create your models here.

class System(models.Model):
    name = models.CharField(max_length=100)
    needs_permit = models.NullBooleanField(default=False)

    primary_economy = models.CharField(max_length=100, null=True)
    population = models.BigIntegerField(default=0, null=True)
    security = models.CharField(max_length=100, null=True)

    allegiance = models.CharField(max_length=100, null=True)
    government = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    faction = models.CharField(max_length=100, null=True)

    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()

    updated_at = models.BigIntegerField()

    def __str__(self):
        return self.name


class Station(models.Model):
    name = models.CharField(max_length=100, null=True)
    system = models.ForeignKey(System, related_name="stations")
    type = models.CharField(max_length=100, null=True)
    max_landing_pad_size = models.CharField(max_length=100, null=True)  # L or M
    distance_to_star = models.BigIntegerField(default=0, null=True)

    allegiance = models.CharField(max_length=100, null=True)
    government = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    faction = models.CharField(max_length=100, null=True)

    has_repair = models.NullBooleanField(default=False)
    has_blackmarket = models.NullBooleanField(default=False)
    has_refuel = models.NullBooleanField(default=False)
    has_rearm = models.NullBooleanField(default=False)
    has_shipyard = models.NullBooleanField(default=False)
    has_outfitting = models.NullBooleanField(default=False)
    has_commodities = models.NullBooleanField(default=False)

    updated_at = models.BigIntegerField()

    def __str__(self):
        return self.name


class Commodity(models.Model):
    name = models.CharField(max_length=100, null=True)
    average_price = models.IntegerField(default=0, null=True)
    category_id = models.IntegerField(default=0, null=True)
    category_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
