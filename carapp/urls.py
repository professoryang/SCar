from django.conf.urls import url, include

from carapp import views

urlpatterns = [

    url(r'^index/', views.index),
    url(r'^registe/', views.registe),
    url(r'^login/', views.login),
    url(r'^logout/', views.logout),
    url(r'^buycar/', views.buycar),
    url(r'^buycarone/', views.buycarone),

]
