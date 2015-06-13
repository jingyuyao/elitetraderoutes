from django.views.generic.base import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = "frontend/base.html"
