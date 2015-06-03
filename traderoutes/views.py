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
    I am dumb. The HTMLFormRenderer was working as intended. The <!-- form.non_field_errors -->
    is always present no matter what to remind us that field exist in the template context.
    The reason the form is showing up as empty for RouteViewSet is because there are no
    edible fields for the form. The form generated can create a new route. However, due to
    the way the related fields are generated, it is not advisable to use HTMLFormRenderer to
    render forms unless we can dynamically limit/search for the choices because the default
    fields will list ALL possible choices.

    Form renderer example usage below.
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

'''
    # Form renderer examples
    renderer_classes = (renderers.JSONRenderer,
                        # renderers.TemplateHTMLRenderer,  # Enable if inserting rendered form into template
                        renderers.BrowsableAPIRenderer,  # Enables .api suffix
                        renderers.HTMLFormRenderer)

    def list(self, request, *args, **kwargs):
        if request.accepted_renderer.format == 'form':
            # Empty form need to use empty serializer
            empty_serializer = self.get_serializer()
            return Response(empty_serializer.data)
        return super(ConnectionViewSet, self).list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        """
        Wraps the get request for an item in a route field.

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        if request.accepted_renderer.format == 'form':
            serializer = self.get_serializer(self.get_object())

            # This will basically render the serialized data as a html form in a string
            # renderer = renderers.HTMLFormRenderer()
            # rendered_form = renderer.render(serializer.data,
            #                                 renderer_context={'request': request, 'template': 'frontend/route.html'})

            # After the string representation of the form is rendered it can be inserted into
            # templates as a variable with autoescape off.
            # response = super(ConnectionViewSet, self).retrieve(request, *args, **kwargs)
            # response.data = {"form": rendered_form}
            # return response

            # Or we can just return a response if using the default form template
            return Response(serializer.data)
        response = super(ConnectionViewSet, self).retrieve(request, *args, **kwargs)
        response.data = {"connection": response.data}
        return response
'''
