from django.conf.urls import url
from . import views


app_name = 'music'   #when we use one or more app use

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view() , name="index"),    #$ represent end of the tab

    # /music/album_id(712)/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),

    # /music/album_id(712)/favorite
    #url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name = 'favorite'),   #view fvr fxn call ,goto view file

]
