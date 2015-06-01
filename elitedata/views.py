from django.shortcuts import render

from rest_framework import viewsets

from common.permissions import IsAdminOrReadOnly
from .models import System, Station, Commodity
from .serializers import StationSerializer, SystemSerializer, CommoditySerializer

# Create your views here.

class SystemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = System.objects.all()
    serializer_class = SystemSerializer


class StationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class CommodityViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer
