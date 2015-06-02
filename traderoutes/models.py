import math

from django.db import models

# Create your models here.

class Route(models.Model):
    """
    Contains the metadata for a trade route.

    Actual stop by stop information is contained as a nested list of Connections.
    """

    owner = models.ForeignKey('auth.User', related_name="routes", editable=False)
    created = models.DateTimeField(auto_now_add=True)  # editable=False automatically

    def __str__(self):
        return "%s:%s" % (str(self.owner), str(self.pk))


class Connection(models.Model):
    """
    Contains the core stop by stop data of trade routes.
    """

    owner = models.ForeignKey('auth.User', related_name="connections", editable=False)
    created = models.DateTimeField(auto_now_add=True)
    route = models.ForeignKey(Route, related_name="connections", editable=False)
    start_system = models.ForeignKey("elitedata.System", related_name="connections_start")
    start_station = models.ForeignKey("elitedata.Station", related_name="connections_start")
    destination_system = models.ForeignKey("elitedata.System", related_name="connections_destination")
    destination_station = models.ForeignKey("elitedata.Station", related_name="connections_destination")
    commodity = models.ForeignKey("elitedata.Commodity", related_name='connections')
    buy_price = models.IntegerField(default=0)
    sell_price = models.IntegerField(default=0)
    supply = models.IntegerField(default=0)
    demand = models.IntegerField(default=0)

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