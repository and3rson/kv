from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<group_pk>[\w\d_]+)$', views.group),
    url(r'^(?P<group_pk>[\d\w_]+)/(?P<record_pk>[\d\w_]+)$', views.record),
]
