from django.conf.urls import url , handler404,handler500
from . import views

urlpatterns = [
    url(r'^$', views.category, name='category'),
    url(r'(?P<category_id>\d)/$', views.cakeList, name='cakeList'),
    url(r'(?P<cake_id>\d+)/detail/$', views.cakeDetail, name='detail'),
]
handler403 = views.page_not_find
handler404 = views.page_not_find
handler500 = views.page_not_find