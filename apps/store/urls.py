from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^curate/', views.curate, name = "curate"),
    url(r'^create_merch/', views.create_merch, name = "create_merch"),
    url(r'^add_to_cart/(?P<id>\d+)/', views.add_to_cart, name = "add_to_cart"),
    url(r'^show_cart/', views.show_cart, name = "show_cart"),
    url(r'^pay/', views.pay, name= "pay"),
    url(r'^delete/(?P<id>\d+)/', views.delete, name= "delete"),
    url(r'^remove_from_cart/(?P<id>\d+)/', views.remove_from_cart, name = 'remove_from_cart')
]
