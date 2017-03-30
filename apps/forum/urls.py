from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = "index"),
    url(r'^(?P<id>\d+)/post$', views.post, name = "post"),
    url(r'^add$', views.add, name = "add"),
    url(r'^(?P<id>\d+)/comment$', views.comment, name = "comment"),
    url(r'^next$', views.next, name = "next"),
    url(r'^previous$', views.previous, name = "previous"),
    url(r'^(?P<id>\d+)/nextcomment$', views.nextcomment, name = "nextcomment"),
    url(r'^(?P<id>\d+)/previouscomment$', views.previouscomment, name = "previouscomment"),
    url(r'^(?P<id>\d+)/init$', views.init, name = "init"),
    url(r'^page/(?P<id>\d+)$', views.page, name = "page"),
    url(r'^(?P<id>\d+)/page/(?P<page>\d+)$', views.commentpage, name = "commentpage"),
    url(r'^back', views.back, name = "back"),
    url(r'^(?P<id>\d+)/post/delete', views.delete, name = "delete"),
    url(r'^(?P<id>\d+)/comment/(?P<comment>\d+)/delete', views.delcom, name = "delcom"),
]
