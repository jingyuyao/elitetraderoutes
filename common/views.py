from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import filters

from common.serializers import UserSerializer

response_wrapper_name = "data"

def wrap_response(response):
        """
        Wraps the data of the response in a top level field specified by self.response_wrapper_name

        :param response:
        :return:
        """
        response.data = {response_wrapper_name: response.data}
        return response


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ResponseWrapperMixin(object):
    """
    Wraps all responses in a top level data field and force render validation error details.

    This is useful for passing objects returned by the serializer as
    just one variable.
    """

    def list(self, request, *args, **kwargs):
        return wrap_response(super(ResponseWrapperMixin, self).list(request, *args, **kwargs))

    def create(self, request, *args, **kwargs):
        # So the problem is that when the error is raise out of this class, DRF no longer
        # renders the response unto our template. Instead, it renders django's default 400 view
        # which do not spit out any nice data. One way to fix it is to catch the validation
        # error here and returns the wrapped response.
        try:
            return wrap_response(super(ResponseWrapperMixin, self).create(request, *args, **kwargs))
        except ValidationError as e:
            return wrap_response(Response(e.detail, status=e.status_code))

    def retrieve(self, request, *args, **kwargs):
        return wrap_response(super(ResponseWrapperMixin, self).retrieve(request, *args, **kwargs))

    def update(self, request, *args, **kwargs):
        return wrap_response(super(ResponseWrapperMixin, self).update(request, *args, **kwargs))

    def destroy(self, request, *args, **kwargs):
        return wrap_response(super(ResponseWrapperMixin, self).destroy(request, *args, **kwargs))


class WrappedModelViewSet(ResponseWrapperMixin, viewsets.ModelViewSet):
    """
    The base for all the ModelViewSets used in the project.

    All responses are wrapped in a data field and ValidationError data is passed to the
    intended template. Also enables both DjangoFilterBackend and SearchFilter to do filter
    duties.
    """
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter)
    pass

# def wrapped_exception_handler(exec, context):
#     """
#     This wraping does not solve the problem of response not being rendered unto the template.
#
#     :param exec:
#     :param context:
#     :return:
#     """
#     response = exception_handler(exec, context)
#
#     if response is not None:
#         return wrap_response(response)
#
#     return response
