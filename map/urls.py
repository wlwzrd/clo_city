from django.conf.urls import url, include
from map import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<id>[a-zA-Z0-9-_.]+)/$', views.neighborhoods, name='neighborhood'),
    url(r'^(?P<id>[a-zA-Z0-9-_.]+)/barrio/(?P<neighborhood>[a-zA-Z0-9-_.]+)/$', views.commerces, name='commerces'),

    
]
