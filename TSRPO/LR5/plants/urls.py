from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^division/(?P<division_id>[0-9]+)/$', views.plants_in_division, name='plants_in_division'),
    url(r'^division/(?P<division_id>[0-9]+)/add$', views.plant_add, name='plant_add'),
    url(r'^division/[0-9]+/plant/(?P<plant_id>[0-9]+)/edit$', views.plant_edit, name='plant_edit'),
    url(r'^division/(?P<division_id>[0-9]+)/plant/(?P<plant_id>[0-9]+)/put$', views.plant_put, name='plant_put'),
    url(r'^division/(?P<division_id>[0-9]+)/plant/(?P<plant_id>[0-9]+)/delete$', views.plant_delete, name='plant_delete'),
    url(r'^division/[0-9]+/plant/(?P<plant_id>[0-9]+)/ajax_delete$', views.ajax_plant_delete, name='ajax_plant_delete'),
    url(r'^division/(?P<division_id>[0-9]+)/ajax_partial_load$', views.ajax_partial_load, name='ajax_partial_load'),
]
