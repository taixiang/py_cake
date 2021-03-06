"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, handler403, handler404, handler500
from django.contrib import admin
from cake import views
from rest_framework import routers
from django.views.generic.base import TemplateView

router = routers.DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'cakelist', views.CakeListViewSet)
router.register(r'detail', views.DetailViewSet, base_name='detail')

urlpatterns = [
    url(r'^cake/', include('cake.urls', namespace='cake', app_name='cake')),
    url(r'^admin/', admin.site.urls),
    url(r'^spider/', include('spider.urls', namespace='spider', app_name='spider')),
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^vue/', TemplateView.as_view(template_name="test.html")),

]
handler403 = views.page_not_find
handler404 = views.page_not_find
handler500 = views.page_not_find
