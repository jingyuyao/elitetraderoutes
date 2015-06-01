from rest_framework import serializers

from .models import System, Station, Commodity

class SystemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = System


class StationSerializer(serializers.HyperlinkedModelSerializer):

    # Painful debugging note: HyperlinkedIdentityField forcefully sets its queryset to the model
    system = serializers.HyperlinkedRelatedField(view_name='system-detail', read_only=True)

    class Meta:
        model = Station


class CommoditySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Commodity