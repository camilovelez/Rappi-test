from django.conf.urls import url
from . import views
from . import controller

urlpatterns=[
    url(r'^$', views.home),
    url(r'^operate_cube$', controller.operate_cube),
]