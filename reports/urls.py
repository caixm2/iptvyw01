from django.conf.urls import url

from . import views

app_name = 'reports'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^usrs_in_ippool/$', views.usrs_in_ippool, name = 'usrs_in_ippool'),
]