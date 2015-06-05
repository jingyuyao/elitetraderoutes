from rest_framework.decorators import detail_route
from rest_framework.response import Response
from rest_framework import filters

from .models import System, Station, Commodity
from .serializers import CommoditySerializer, StationSerializer, SystemSerializer, MinimizedSystemSerializer

import django_filters

from common.views import WrappedModelViewSet, wrap_response

# Create your views here.

class SystemViewSet(WrappedModelViewSet):
    queryset = System.objects.all()
    serializer_class = SystemSerializer
    search_fields = ('name',)

    @detail_route()
    def stations(self, request, pk=None):
        """
        A route to display only the stations this System contains.

        :param request:
        :param pk:
        :return:
        """
        system = self.get_object()
        stations = Station.objects.filter(system=system)

        serializer = StationSerializer(stations, context={'request': request}, many=True)
        return wrap_response(Response(serializer.data))

    @detail_route()
    def min(self, request, pk=None):
        """
        A route to display the minimized System view.

        :param request:
        :param pk:
        :return:
        """
        serializer = MinimizedSystemSerializer(self.get_object(), context={'request': request})

        return wrap_response(Response(serializer.data))


class StationViewSet(WrappedModelViewSet):
    class StationFilter(django_filters.FilterSet):
        distance_to_star = django_filters.NumberFilter(lookup_type='lt')

        class Meta:
            model = Station
            fields = ('distance_to_star',)

    queryset = Station.objects.all()
    serializer_class = StationSerializer
    filter_class = StationFilter
    search_fields = ('name', )


class CommodityViewSet(WrappedModelViewSet):
    class CommodityFilter(django_filters.FilterSet):
        average_price = django_filters.NumberFilter(lookup_type='lt')
        name = django_filters.CharFilter(lookup_type='icontains')

        class Meta:
            model = Commodity
            fields = ('average_price', 'name')

    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer
    filter_class = CommodityFilter
    search_fields = ('name',)
