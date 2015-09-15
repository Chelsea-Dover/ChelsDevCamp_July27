from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.jqjavapic, name='jqavapic'),
    url(r'^join', views.jqoin, name='join'),
    url(r'^gallery', views.jqgallery, name='gallery')

]