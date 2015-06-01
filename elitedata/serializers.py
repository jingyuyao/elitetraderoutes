from rest_framework import serializers

from .models import System, Station, Commodity


class CommoditySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Commodity


class StationSerializer(serializers.HyperlinkedModelSerializer):

    # Painful debugging note: HyperlinkedIdentityField forcefully sets its queryset to the model
    system = serializers.HyperlinkedRelatedField(view_name='system-detail', read_only=True)

    class Meta:
        model = Station


class SystemSerializer(serializers.HyperlinkedModelSerializer):
    # stations = serializers.HyperlinkedRelatedField(view_name='station-detail', many=True, read_only=True)

    stations = StationSerializer(many=True, read_only=True)

    # Decided to go with nested relation with read_only enable because the OPTIONS request for
    # relatedfield causes errors and this way saves the number of requests needed to get the complete
    # description of a system.

    class Meta:
        model = System