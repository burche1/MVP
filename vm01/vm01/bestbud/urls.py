from django.conf.urls import url
from django.contrib import admin
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^check_age/$', TemplateView.as_view(template_name='bestbud/check_age.html')),
    url(r'^check_age/$', views.check_age, name='check_age'),
    #url(r'^boas-vindas/$', views.boas_vindas, {'template_name': 'bestbud/boas-vindas.html'}, name='boas-vindas'),
    url(r'^check_age/produtos/$', views.produtos, name='produtos'),
]
