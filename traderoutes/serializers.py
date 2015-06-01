from rest_framework import serializers
from django.utils import timezone

from .models import Route, Connection
from elitedata.models import Station, System, Commodity


class RouteSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source="owner.username")
    owner = serializers.HyperlinkedIdentityField(view_name='user-detail')
    created = serializers.DateTimeField(read_only=True)
    connections = serializers.HyperlinkedIdentityField(view_name='connection-detail', many=True)

    class Meta:
        model = Route
        fields = ('url', 'owner', 'created', 'connections')


class ConnectionSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.HyperlinkedIdentityField(view_name='user-detail')
    created = serializers.DateTimeField(read_only=True)
    route = serializers.HyperlinkedRelatedField(view_name='route-detail', queryset=Route.objects.all())
    start_system = serializers.HyperlinkedRelatedField(view_name='system-detail', queryset=System.objects.all())
    start_station = serializers.HyperlinkedRelatedField(view_name='station-detail', queryset=Station.objects.all())
    destination_system = serializers.HyperlinkedRelatedField(view_name='system-detail', queryset=System.objects.all())
    destination_station = serializers.HyperlinkedRelatedField(view_name='station-detail', queryset=Station.objects.all())
    commodity = serializers.HyperlinkedRelatedField(view_name='commodity-detail', queryset=Commodity.objects.all())

    class Meta:
        model = Connection
        fields = ('url',
                  'owner', 'created', 'route',
                  'start_system', 'start_station',
                  'destination_system', 'destination_station',
                  'commodity', 'buy_price', 'sell_price', 'supply', 'demand')


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
