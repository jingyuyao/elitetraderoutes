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
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    renderer_classes = (renderers.JSONRenderer, renderers.TemplateHTMLRenderer,
                        renderers.BrowsableAPIRenderer, renderers.HTMLFormRenderer)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        response = super(RouteViewSet, self).list(request, *args, **kwargs)
        template_name = 'route_list'
        return Response({template_name: response.data}, template_name='frontend/%s.html' % template_name)

    def retrieve(self, request, *args, **kwargs):
        response = super(RouteViewSet, self).retrieve(request, *args, **kwargs)
        template_name = 'route'
        return Response({template_name: response.data}, template_name='frontend/%s.html' % template_name)

    @list_route()
    def form(self, request, *args, **kwargs):
        serializer = self.get_serializer()
        renderer = renderers.HTMLFormRenderer()
        form_html = renderer.render(serializer.data, renderer_context={
            'request': request
        })
        print(form_html)
        return HttpResponse(form_html)

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