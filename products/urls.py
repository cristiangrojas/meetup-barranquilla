from django.conf.urls import include, url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^.*$', TemplateView.as_view(template_name='products/index.html'), name='index'),
]