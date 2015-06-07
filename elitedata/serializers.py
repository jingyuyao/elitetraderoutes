from rest_framework import serializers

from .models import System, Station, Commodity
from common.serializers import IDHyperlinkedModelSerializer


class CommoditySerializer(IDHyperlinkedModelSerializer):
    """Detailed serializer for Commodity.
    """

    class Meta:
        model = Commodity


class StationSerializer(IDHyperlinkedModelSerializer):
    """
    Serializer for Station.

    Decision was made to not include detailed System information as nested field.
    Although it would be useful to have the System information from one request
    to the station, the System is technically not inside a Station. The System
    and Station is a has-a relationship.
    """

    # Painful debugging note: HyperlinkedIdentityField forcefully sets its queryset to the model
    system = serializers.HyperlinkedRelatedField(view_name='system-detail', read_only=True)
    system_name = serializers.ReadOnlyField(source="system.name")

    class Meta:
        model = Station


class SystemSerializer(IDHyperlinkedModelSerializer):
    """
    Detailed serializer for System.

    Includes the details of each Station in the System as represented by the
    StationSerializer. Since Stations only exists in System, it forms a has-a
    relationship with the System. A detailed description of the System is the
    default since we are assuming most requests to get System information
    do not already have the Station information in hand.
    """

    # Nested relation
    stations = StationSerializer(many=True, read_only=True)

    class Meta:
        model = System


class MinimizedSystemSerializer(IDHyperlinkedModelSerializer):
    """
    Minimized serializer for System.

    Does not include details for each Station.
    """

    stations = serializers.HyperlinkedRelatedField(view_name='station-detail', many=True, read_only=True)

    class Meta:
        model = System
