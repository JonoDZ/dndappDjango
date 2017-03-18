from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^shop/$', views.shop, name='shop'),
    url(r'^update/$', views.update, name='update'),
    url(r'^get_name/$', views.get_name, name='get_name'),
    url(r'^(?P<npcsToGen>[0-9]+)/regennpcs/$', views.regenNpcs, name='regenNpcs'),
]