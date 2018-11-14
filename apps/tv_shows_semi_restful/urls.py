from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
  url(r'^$', views.index),
  url(r'^new$', views.display_add_show),
  url(r'^create_show$', views.create_show),
  url(r'^(?P<number>[0-9]+)/edit$', views.view_edit_show),
  url(r'^edit_show/(?P<number>[0-9]+)$', views.edit_show),
  url(r'^(?P<number>[0-9]+)$', views.display_show),
  url(r'^(?P<number>[0-9]+)/delete$', views.delete_show),
]