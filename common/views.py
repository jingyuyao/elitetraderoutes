from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.viewsets import mixins

from common.serializers import UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ResponseWrapperMixin(object):
    """
    Wraps all responses in a top level data field.

    This is useful for passing objects returned by the serializer as
    just one variable.
    """

    response_wrapper_name = "data"

    def list(self, request, *args, **kwargs):
        return self.wrap_response(super(ResponseWrapperMixin, self).list(request, *args, **kwargs))

    def create(self, request, *args, **kwargs):
        return self.wrap_response(super(ResponseWrapperMixin, self).create(request, *args, **kwargs))

    def retrieve(self, request, *args, **kwargs):
        return self.wrap_response(super(ResponseWrapperMixin, self).retrieve(request, *args, **kwargs))

    def update(self, request, *args, **kwargs):
        return self.wrap_response(super(ResponseWrapperMixin, self).update(request, *args, **kwargs))

    def destroy(self, request, *args, **kwargs):
        return self.wrap_response(super(ResponseWrapperMixin, self).destroy(request, *args, **kwargs))

    def wrap_response(self, response):
        """
        Wraps the data of the response in a top level field specified by self.response_wrapper_name

        :param response:
        :return:
        """
        response.data = {self.response_wrapper_name: response.data}
        return response


class WrappedModelViewSet(ResponseWrapperMixin, viewsets.ModelViewSet):
    """
    Convenience ModelViewSet class that implements the ResponseWrapperMixin
    """
    pass
