from rest_framework import serializers

from .models import System, Station, Commodity

class SystemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = System


class StationSerializer(serializers.HyperlinkedModelSerializer):
    system = serializers.HyperlinkedIdentityField(view_name='system-detail')

    class Meta:
        model = Station


class CommoditySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Commodity