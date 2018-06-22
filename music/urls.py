from django.conf.urls import url
from . import views


app_name = 'music'   #when we use one or more app use

urlpatterns = [
    # /music/
    url(r'^$', views.index , name="index"),    #$ represent end of the tab

# /music/album_id(712)/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name = 'detail'),
]
