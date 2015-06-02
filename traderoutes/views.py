from django.http.response import HttpResponse

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import renderers

from .permissions import IsOwnerOrReadOnly
from .models import Route, Connection
from .serializers import ConnectionSerializer, RouteSerializer, MinimizedRouteSerializer

# Create your views here.

class RouteViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Route.

    Notes:
    Decided to not wrap the response objects in a top level variable to preserve
    the consistency in the API.

    HTMLFormRenderer is ill documented. Spent half a night trying to use it.
    Put it off and just build our own form for now
    """
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    renderer_classes = (renderers.JSONRenderer,
                        renderers.TemplateHTMLRenderer,
                        renderers.BrowsableAPIRenderer,  # Enables .api suffix
                        )
    template_name = "frontend/route.html"  # The default template for all html actions

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        """
        Wraps the get request for an item in a route field.

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        response = super(RouteViewSet, self).retrieve(request, *args, **kwargs)
        response.data = {"route": response.data}
        return response

    def create(self, request, *args, **kwargs):
        response = super(RouteViewSet, self).create(request, *args, **kwargs)
        response.data = {"route": response.data}
        return response

    @detail_route()
    def min(self, request, pk=None):
        """
        Displays a minimized route inforamtion without the details of each connection.

        :param request:
        :param pk:
        :return:
        """
        serializer = MinimizedRouteSerializer(self.get_object(), context={'request': request})

        return Response(serializer.data)


class ConnectionViewSet(viewsets.ModelViewSet):
    queryset = Connection.objects.all()
    serializer_class = ConnectionSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)