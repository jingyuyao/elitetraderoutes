from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('systems', views.SystemViewSet)
router.register('stations', views.StationViewSet)
router.register('commodities', views.CommodityViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]