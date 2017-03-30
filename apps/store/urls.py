from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = "index"),
<<<<<<< HEAD
#     url(r'^curate$', views.curate, name = "curate"),
#     url(r'^create_merch$', views.create_merch, name = "create_merch"),
#     url(r'^add_to_cart/(?P<id>\d+)$', views.add_to_cart, name = "add_to_cart")
 ]
=======
    url(r'^curate$', views.curate, name = "curate"),
    url(r'^create_merch$', views.create_merch, name = "create_merch"),
    url(r'^add_to_cart/(?P<id>\d+)$', views.add_to_cart, name = "add_to_cart"),
    url(r'^show_cart$', views.show_cart, name = "show_cart"),
    url(r'^pay$', views.pay, name= "pay"),
    url(r'^remove_from_cart/(?P<id>\d+)$', views.remove_from_cart, name = 'remove_from_cart')
]
>>>>>>> c815dd9df220a416e746797e52da6c9362009afc
