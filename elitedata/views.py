from django.shortcuts import render

from rest_framework import viewsets

from common.permissions import IsAdminOrReadOnly
from .models import System, Station, Commodity
from .serializers import StationSerializer, SystemSerializer, CommoditySerializer

# Create your views here.

class SystemViewSet(viewsets.ModelViewSet):
    queryset = System.objects.all()
    serializer_class = SystemSerializer
    permission_classes = (IsAdminOrReadOnly,)


class StationViewSet(viewsets.ModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CommodityViewSet(viewsets.ModelViewSet):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer
    permission_classes = (IsAdminOrReadOnly,)
