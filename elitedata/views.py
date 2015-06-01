from django.shortcuts import render, get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from .models import System, Station, Commodity
from .serializers import StationSerializer, SystemSerializer, CommoditySerializer

# Create your views here.

class SystemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = System.objects.all()
    serializer_class = SystemSerializer

    @detail_route()
    def stations(self, request, pk=None):
        system = self.get_object()
        stations = Station.objects.filter(system=system)

        serializer = StationSerializer(stations, context={'request': request}, many=True)
        return Response(serializer.data)


class StationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class CommodityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer
