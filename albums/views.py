from django.shortcuts import render
from .models import Album
# from .forms import Albumform

# Create your views here.
def list_albums(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html",
                  {"albums": albums})


def add_Album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/add_Album.html", {"form": form})


def edit_Album(request, pk):
    Album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=Album)
    else:
        form = AlbumForm(data=request.POST, instance=Album)
        if form.is_valid():
            form.save()
            return redirect(to='list_albums')

    return render(request, "albums/edit_Album.html", {
        "form": form,
        "Album": Album
    })


def delete_Album(request, pk):
    Album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        Album.delete()
        return redirect(to='list_albums')

    return render(request, "albums/delete_Album.html",
                  {"Album": Album})