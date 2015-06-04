from rest_framework.decorators import detail_route
from rest_framework.response import Response

from .models import System, Station, Commodity
from .serializers import CommoditySerializer, StationSerializer, SystemSerializer, MinimizedSystemSerializer

from common.views import WrappedModelViewSet

# Create your views here.

class SystemViewSet(WrappedModelViewSet):
    queryset = System.objects.all()
    serializer_class = SystemSerializer

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
        return self.wrap_response(Response(serializer.data))

    @detail_route()
    def min(self, request, pk=None):
        """
        A route to display the minimized System view.

        :param request:
        :param pk:
        :return:
        """
        serializer = MinimizedSystemSerializer(self.get_object(), context={'request': request})

        return self.wrap_response(Response(serializer.data))


class StationViewSet(WrappedModelViewSet):
    queryset = Station.objects.all()
    serializer_class = StationSerializer


class CommodityViewSet(WrappedModelViewSet):
    queryset = Commodity.objects.all()
    serializer_class = CommoditySerializer
