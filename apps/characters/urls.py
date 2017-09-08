from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^profile/', views.profile, name = "profile"),
    url(r'^create/', views.create, name = "create"),
    url(r'^createAttb/', views.createAttb, name = "createAttb"),
    url(r'^charCreate/', views.charCreate, name = "charCreate"),
]
