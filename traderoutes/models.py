import math

from django.db import models
from django.utils import timezone

# Create your models here.

class Route(models.Model):
    owner = models.ForeignKey('auth.User', related_name="routes")
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "%s:%s" % (str(self.owner), str(self.pk))


class Connection(models.Model):
    owner = models.ForeignKey('auth.User', related_name="connections")
    created = models.DateTimeField(default=timezone.now)
    route = models.ForeignKey(Route, related_name="connections")
    start_system = models.ForeignKey("elitedata.System", related_name="connections_start")
    start_station = models.ForeignKey("elitedata.Station", related_name="connections_start")
    destination_system = models.ForeignKey("elitedata.System", related_name="connections_destination")
    destination_station = models.ForeignKey("elitedata.Station", related_name="connections_destination")
    commodity = models.ForeignKey("elitedata.Commodity", related_name='connections')
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

    def __str__(self):
        return "%s:%s->%s:%s" % (str(self.start_system), str(self.start_station),
                                 str(self.destination_system), str(self.destination_station))