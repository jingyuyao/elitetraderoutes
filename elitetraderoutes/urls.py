"""elitetraderoutes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

import common.views
import traderoutes.views
import elitedata.views

api_router = DefaultRouter()
api_router.register('route', traderoutes.views.RouteViewSet)
api_router.register('connection', traderoutes.views.ConnectionViewSet)
api_router.register('user', common.views.UserViewSet)
api_router.register('system', elitedata.views.SystemViewSet)
api_router.register('station', elitedata.views.StationViewSet)
api_router.register('commodity', elitedata.views.CommodityViewSet)

urlpatterns = [
    url(r'^index/', include('frontend.urls')),
    url(r'^', include(api_router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
