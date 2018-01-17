from django.conf.urls import url , handler404,handler500
from . import views

urlpatterns = [
    url(r'^$', views.appUrl, name='appUrl'),

]
