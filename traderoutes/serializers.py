from rest_framework import serializers
from django.utils import timezone

from .models import Route, Connection


class RouteSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source="owner.username")
    owner = serializers.HyperlinkedIdentityField(view_name='user-detail')

    class Meta:
        model = Route


class ConnectionSerializer(serializers.HyperlinkedModelSerializer):
    route = serializers.HyperlinkedIdentityField(view_name='route-detail')
    start_system = serializers.HyperlinkedIdentityField(view_name='system-detail')
    start_station = serializers.HyperlinkedIdentityField(view_name='station-detail')
    destination_system = serializers.HyperlinkedIdentityField(view_name='system-detail')
    destination_station = serializers.HyperlinkedIdentityField(view_name='station-detail')
    commodity = serializers.HyperlinkedIdentityField(view_name='commodity-detail')

    class Meta:
        model = Connection
