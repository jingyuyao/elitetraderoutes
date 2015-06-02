from django.shortcuts import render

from django.views.generic import DetailView
from django.views.generic.base import TemplateView

from traderoutes.models import Route, Connection

# Create your views here.

class IndexView(TemplateView):
    template_name = "frontend/base.html"
