from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_name/$', views.get_name, name='get_name'),
    url(r'^test/$', views.test, name='test'),
]