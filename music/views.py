#used Generic views
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album

class IndexView(generic.ListView):
    template_name='music/index.html'
    context_object_name = 'all_album'

    def get_queryset(self):
        return Album.objects.all()

class DetailView(generic.DetailView):
    model= Album
    template_name = 'music/detail.html'