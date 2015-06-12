from django.shortcuts import redirect

from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response
from rest_framework import renderers

from .permissions import IsOwnerOrReadOnly
from .models import Route, Connection
from .serializers import ReadConnectionSerializer, WriteConnectionSerializer,\
    RouteSerializer, MinimizedRouteSerializer

from common.views import WrappedModelViewSet, wrap_response

# Create your views here.

class RouteViewSet(WrappedModelViewSet):
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
    template_name = "frontend/route/instance.html"  # The default template for all html actions

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        response = super(RouteViewSet, self).list(request, *args, **kwargs)
        response.template_name = "frontend/route/list.html"
        return response

    @detail_route()
    def min(self, request, *args, **kwargs):
        """
        Displays a minimized route information without the details of each connection.

        :param request:
        :param pk:
        :return:
        """
        serializer = MinimizedRouteSerializer(instance=self.get_object(), context={'request': request})
        return wrap_response(Response(serializer.data))


class ConnectionViewSet(WrappedModelViewSet):
    queryset = Connection.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)
    renderer_classes = (renderers.JSONRenderer,
                        renderers.TemplateHTMLRenderer,
                        renderers.BrowsableAPIRenderer,  # Enables .api suffix
                        )
    template_name = "frontend/connection/instance.html"
    search_fields = ("start_system", 'destination_system')

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ReadConnectionSerializer
        else:
            return WriteConnectionSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def list(self, request, *args, **kwargs):
        response = super(ConnectionViewSet, self).list(request, *args, **kwargs)
        response.template_name = "frontend/connection/list.html"
        return response


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
            #                                 renderer_context={'request': request, 'template': 'frontend/instance.html'})

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
