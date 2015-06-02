from rest_framework import serializers

from .models import Route, Connection
from elitedata.models import Station, System, Commodity


class ConnectionSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Connection class.

    This serializer will validate start and destination stations belong in the specified
    start and destination system.

    Note:
    The queryset for the system and station fields encompasses all of the objects in their
    respective model. This makes the default API view extremely slow as it will load up all
    the possible choices for selection in the view. It does not affect normal json calls.
    """

    owner = serializers.HyperlinkedIdentityField(view_name='user-detail')
    created = serializers.DateTimeField(read_only=True)
    route = serializers.HyperlinkedRelatedField(view_name='route-detail', queryset=Route.objects.all())
    start_system = serializers.HyperlinkedRelatedField(view_name='system-detail', queryset=System.objects.all())
    start_station = serializers.HyperlinkedRelatedField(view_name='station-detail',
                                                        queryset=Station.objects.all())
    destination_system = serializers.HyperlinkedRelatedField(view_name='system-detail', queryset=System.objects.all())
    destination_station = serializers.HyperlinkedRelatedField(view_name='station-detail',
                                                              queryset=Station.objects.all())
    commodity = serializers.HyperlinkedRelatedField(view_name='commodity-detail', queryset=Commodity.objects.all())
    distance = serializers.SerializerMethodField()  # Read only

    @staticmethod
    def get_distance(obj):
        return obj.distance()

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

    class Meta:
        model = Connection
        fields = ('url',
                  'owner', 'created', 'route',
                  'start_system', 'start_station',
                  'destination_system', 'destination_station',
                  'distance',
                  'commodity', 'buy_price', 'sell_price', 'supply', 'demand')


class RouteSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for the Route class.

    Includes a read only field of all the connections the route has.
    """

    owner = serializers.HyperlinkedIdentityField(view_name='user-detail')
    created = serializers.DateTimeField(read_only=True)
    connections = ConnectionSerializer(many=True, read_only=True)

    # Decided to go with nested relation with read_only enable because the OPTIONS request for
    # relatedfield causes errors and this way saves the number of requests needed to get the complete
    # description of a route.

    class Meta:
        model = Route
        fields = ('url', 'owner', 'created', 'connections')


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
