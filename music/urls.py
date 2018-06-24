from django.conf.urls import url
from . import views


app_name = 'music'   #when we use one or more app use

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view() , name="index"),    #$ represent end of the tab

    url(r'^register/$', views.UserFormView.as_view() , name="register"),

    # /music/album_id(712)/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),

    # /music/album_id(712)/favorite
    #url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name = 'favorite'),   #view fvr fxn call ,goto view file

    #/music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album_add'),

    # /music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album_update'),

    # /music/album/add/
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album_delete'),

]

