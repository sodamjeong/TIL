from django.shortcuts import render,redirect
from .models import Album
from .forms import AlbumForm

# Create your views here.

def album(request):
    context = {
        'albums': Album.objects.order_by('-pk'),
        'form' : AlbumForm()
    }
    return render(request,'album.html', context)

def create(request):
        form = AlbumForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('albums:album')

