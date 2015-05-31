import math

from django.db import models
from django.utils import timezone

# Create your models here.

class Route(models.Model):
    owner = models.ForeignKey('auth.User', related_name="route")
    created = models.DateTimeField(default=timezone.now)


class Connection(models.Model):
    route = models.ForeignKey(Route)
    start_system = models.ForeignKey("elitedata.System", related_name="connection_start")
    start_station = models.ForeignKey("elitedata.Station", related_name="connection_start")
    destination_system = models.ForeignKey("elitedata.System", related_name="connection_destination")
    destination_station = models.ForeignKey("elitedata.Station", related_name="connection_destination")
    commodity = models.ForeignKey("elitedata.Commodity")
    buy_price = models.IntegerField()
    sell_price = models.IntegerField()
    supply = models.IntegerField()
    demand = models.IntegerField()

    def profit_per_ton(self):
        return self.sell_price - self.buy_price

    def distance(self):
        s = self.start_system
        e = self.destination_system
        # The distance formula
        return math.sqrt((s.x+e.x)**2 + (s.y+e.y)**2 + (s.z+e.z)**2)
