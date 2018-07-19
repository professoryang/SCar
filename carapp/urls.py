from django.conf.urls import url, include

from carapp import views

urlpatterns = [

    url(r'^index/', views.index),
    url(r'^registe/', views.registe),
    url(r'^login/', views.login),
    url(r'^yzm/', views.yzm),
    url(r'^logout/', views.logout),
]
