from django.conf.urls import url
from . import views

app_name = 'bookmark'
urlpatterns = [
        url(r'^$', views.BookmarkLV.as_view(), name='index'),
        url(r'^(?P<pk>[0-9]+)/$', views.BookmarkDV.as_view(), name='BookmarkDetail'),
]
