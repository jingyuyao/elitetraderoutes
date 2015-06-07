from rest_framework import serializers

from .models import Route, Connection
from elitedata.models import Station, System, Commodity
from elitedata.serializers import MinimizedSystemSerializer, StationSerializer, CommoditySerializer
from common.serializers import IDHyperlinkedModelSerializer

class BaseConnectionSerializer(IDHyperlinkedModelSerializer):
    """
    Base serializer for Connection model.
    """
    route = serializers.HyperlinkedRelatedField(view_name='route-detail', queryset=Route.objects.all())

    class Meta:
        model = Connection


class WriteConnectionSerializer(BaseConnectionSerializer):
    """
    The write serializer for the Connection class.

    This serializer will validate start and destination stations belong in the specified
    start and destination system.

    Note:
    The queryset for the system and station fields encompasses all of the objects in their
    respective model. This makes the default API view extremely slow as it will load up all
    the possible choices for selection in the view. It does not affect normal json calls.
    """

    start_system = serializers.HyperlinkedRelatedField(view_name='system-detail', queryset=System.objects.all())
    start_station = serializers.HyperlinkedRelatedField(view_name='station-detail', queryset=Station.objects.all())
    destination_system = serializers.HyperlinkedRelatedField(view_name='system-detail', queryset=System.objects.all())
    destination_station = serializers.HyperlinkedRelatedField(view_name='station-detail', queryset=Station.objects.all())
    commodity = serializers.HyperlinkedRelatedField(view_name='commodity-detail', queryset=Commodity.objects.all())

    def validate(self, data):
        """
        Make sure start and destination stations are in start and destination systems, respectively.

        :param data:
        :return:
        """

        self._validate_station(data['start_system'], data['start_station'])
        self._validate_station(data['destination_system'], data['destination_station'])

        return data

    @staticmethod
    def _validate_station(system, station):
        """
        Validates whether 'station' is in 'system'.

        :param system:
        :param station:
        :return:
        """
        if station not in Station.objects.filter(system=system):
            raise serializers.ValidationError("Station(%s) not in system(%s)." % (str(station), str(system)))

class ReadConnectionSerializer(BaseConnectionSerializer):
    """
    The read serializer for the Connection model.

    This serializer shows the referenced models as nested objects.
    """
    start_system = MinimizedSystemSerializer()
    start_station = StationSerializer()
    destination_system = MinimizedSystemSerializer()
    destination_station = StationSerializer()
    commodity = CommoditySerializer()

    distance = serializers.SerializerMethodField()  # Read only

    @staticmethod
    def get_distance(obj):
        return obj.distance()

class BaseRouteSerializer(IDHyperlinkedModelSerializer):
    """
    Base serializer for Route. Sub-class need to provide value for connections
    """

    @property
    def connections(self):
        """
        A serializer for Connection
        """
        raise NotImplementedError

    class Meta:
        model = Route


class RouteSerializer(BaseRouteSerializer):
    """
    Serializer for the Route.

    Includes detailed information on all the Connection the Route has.
    """

    connections = ReadConnectionSerializer(many=True, read_only=True)


class MinimizedRouteSerializer(BaseRouteSerializer):
    """
    Minimized serializer for Route.

    Only contains a link each Connection the Route has.
    """

    connections = serializers.HyperlinkedRelatedField(view_name="connection-detail", many=True, read_only=True)


"""
Why not use primary key relationships?
- Avoids building URL
- No way to misrepresent information
"""


# class ConnectionSerializer(serializers.ModelSerializer):
#     route = serializers.PrimaryKeyRelatedField(queryset=Route.objects.all())
#     start_system = serializers.PrimaryKeyRelatedField(queryset=System.objects.all())
#     start_station = serializers.PrimaryKeyRelatedField(queryset=Station.objects.all())
#     destination_system = serializers.PrimaryKeyRelatedField(queryset=System.objects.all())
#     destination_station = serializers.PrimaryKeyRelatedField(queryset=Station.objects.all())
#     commodity = serializers.PrimaryKeyRelatedField(queryset=Commodity.objects.all())
#
#     class Meta:
#         model = Connection
#         fields = ('pk', 'route',
#                   'start_system', 'start_station',
#                   'destination_system', 'destination_station',
#                   'commodity', 'buy_price', 'sell_price', 'supply', 'demand')
