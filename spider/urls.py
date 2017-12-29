from django.conf.urls import url, handler404, handler500
from spider import views

urlpatterns = [
    url(r'^$', views.enList, name='enList'),
    url(r'(?P<enid>\d+)/detail/$', views.enDetail, name='detail'),
    url(r'^enList_json/$', views.enList_json, name='enList_json'),
]
