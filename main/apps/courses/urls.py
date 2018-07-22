from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^destroy/(?P<id>\d+)$', views.destroy),
    url(r'^destroy/(?P<id>\d+)/delete$', views.delete),
    url(r'^add$', views.add)
]