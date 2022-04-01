from django.conf.urls import url
from django.views.generic import TemplateView

from .api import ProductApi

urlpatterns = [
    url(r'^product/', ProductApi.as_view()),
    url(r'^home', TemplateView.as_view(template_name="autocomplete/home.html")),
]