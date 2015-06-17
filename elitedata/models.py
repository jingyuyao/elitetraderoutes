"""
updated_at is the timestamp from source.
created is the time when the data is added to database.
"""

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
    name = models.CharField(max_length=100)
    system = models.ForeignKey(System, related_name="stations", editable=False)
    type = models.CharField(max_length=100, null=True, blank=True)
    max_landing_pad_size = models.CharField(max_length=100, null=True, blank=True)  # L or M
    distance_to_star = models.BigIntegerField(default=0, null=True, blank=True)  # Might change depending on orbit???

    allegiance = models.CharField(max_length=100, null=True, blank=True)
    government = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    faction = models.CharField(max_length=100, null=True, blank=True)

    has_repair = models.NullBooleanField(default=False, blank=True)
    has_blackmarket = models.NullBooleanField(default=False, blank=True)
    has_refuel = models.NullBooleanField(default=False, blank=True)
    has_rearm = models.NullBooleanField(default=False, blank=True)
    has_shipyard = models.NullBooleanField(default=False, blank=True)
    has_outfitting = models.NullBooleanField(default=False, blank=True)
    has_commodities = models.NullBooleanField(default=False, blank=True)

    updated_at = models.BigIntegerField()

    def __str__(self):
        return self.name


class Commodity(models.Model):
    name = models.CharField(max_length=100)
    average_price = models.IntegerField(default=0, null=True, blank=True)
    category_id = models.IntegerField(default=0, editable=False)
    category_name = models.CharField(max_length=100, editable=False)

    def __str__(self):
        return self.name


class StationCommodity(models.Model):
    commodity = models.ForeignKey(Commodity, related_name='station_commodities', editable=False)
    station = models.ForeignKey(Station, related_name='station_commodities', editable=False)
    buy_price = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    sell_price = models.IntegerField(default=0)
    demand = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s/%s(%i/%i)' % (str(self.station), str(self.commodity), int(self.buy_price), int(self.sell_price))
