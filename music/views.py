#from django.http import Http404             #Raising a 404 HTTP Error
#from django.http import HttpResponse
from django.shortcuts import render , get_object_or_404     ##shortcut function as campare to template package
#from django.template import loader
from .models import Album


def index(request):
    all_album = Album.objects.all()

 #template = loader.get_template('music/index.html')          #create template  and insert html file
    context = {'all_album' : all_album }                          #create dictionary
    #html= ''
    #for album in all_album:                                 #connecting to database
        #url = '/music/' + str(album.id) + "/"
        #html += '<a href = "' + url + ' ">' + album.album_title + '</a></br>'    #insert html code

    return render(request,'music/index.html', context)

def detail(request, album_id):

# when djanngo developer again & again insert number(like 48,45,98) lots of time consume so to reolve this ..
# we use shortcut (get_object_or_404)
    album = get_object_or_404(Album, pk = album_id)   #replaces the entire try exception fxn
    #try:
     #   album = Album.objects.get(pk=album_id)
    #except Album.DoesNotExist:
     #   raise Http404('Album does not exist')
    return render(request , "music/detail.html" , {'album' : album})