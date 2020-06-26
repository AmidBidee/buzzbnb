from django.shortcuts import render, get_object_or_404, redirect
from .models import Song,Artist,Album,Genre,Categorie
from django.views.generic import ListView, DetailView
import datetime

today = datetime.datetime.now()
last_month = today.month - 1 if today.month>2 else 12
last_month_year = today.year if today.month > last_month else today.year - 1


def HomePage(request):
    return render(request, 'base/base.html')

def LatestSongs(request):
    latest_songs = Song.objects.filter(release_date__year=today.year)
    #latest_songs_last_month = Song.objects.filter(release_date__month=last_month)
    return render(request, 'base/list_pages/latest_songs.html', {'latest_songs': latest_songs})

#class LatestSongs(DetailView):
    #model = Song
    #template_name = 'base/list_pages/latest_songs.html'
    #queryset = Song.latest_songs.all()
    #context_object_name = 'latest_songs'


def categorie_or_genre(request):
    return render(request, 'base/categorie_or_genre.html')

class ArtistList(ListView):
    model =  Artist
    context_object_name = 'all_artists'
    template_name = 'base/list_pages/all_artists.html'
    query_pk_and_slug = True

class AllGenres(ListView):
    model = Genre
    context_object_name = 'genres'
    template_name = 'base/list_pages/all_genres.html'

class AllCategories(ListView):
    model = Categorie
    context_object_name = 'categories'
    template_name = 'base/list_pages/all_categories.html'

class SongsByCategorie(DetailView):
    model = Categorie
    template_name = 'base/detail_pages/songs_by_categorie.html'
    context_object_name = 'categories'
    query_pk_and_slug = True

    def get_queryset(self):
        self.categorie = get_object_or_404(Categorie, slug=self.kwargs['slug'])
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_songs"] = Song.objects.filter(categorie=self.categorie)
        print(context['all_songs']) 
        return context
        


class SongsByGenres(DetailView):
    model = Genre
    template_name = 'base/detail_pages/songs_by_genres.html/'
    context_object_name = 'genre'
    query_pk_and_slug = True

    def get_queryset(self):
        self.genre = get_object_or_404(Genre, slug=self.kwargs['slug'])
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_songs"] = Song.objects.filter(genre=self.genre)
        print(context['all_songs'])
        return context
    

class SongDetail(DetailView):
    model = Song
    template_name = 'base/detail_pages/song.html'
    query_pk_and_slug = True

    def get_queryset(self):
        self.song = get_object_or_404(Song, pk=self.kwargs['pk'],
                                              slug=self.kwargs['slug'])
        
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super(SongDetail, self).get_context_data(**kwargs)
        context['songs_by_artist'] = Song.objects.filter(artist=self.song.artist)
        print(context['songs_by_artist'])
        return context

class ArtistDetail(DetailView):
    model = Artist
    template_name = 'base/detail_pages/artist.html'
    query_pk_and_slug = True

    def get_queryset(self):
        self.artist = get_object_or_404(Artist, pk=self.kwargs['pk'], 
                                                slug=self.kwargs['slug'])
        return super().get_queryset()
    

    def get_context_data(self, **kwargs):
        context = super(ArtistDetail, self).get_context_data(**kwargs)
        context['albums'],context['songs'] = (Album.objects.filter(artist=self.artist), 
                                              Song.objects.filter(artist=self.artist))
        print(context['albums'],context['songs'])
        return context

class AlbumDetail(DetailView):
    model = Album
    template_name = 'base/detail_pages/album.html'
    query_pk_and_slug = True

    def get_queryset(self):
        self.album = get_object_or_404(Album, pk=self.kwargs['pk'],
                                              slug=self.kwargs['slug'])
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super(AlbumDetail, self).get_context_data(**kwargs)
        context['tracks'] = Song.objects.filter(album=self.album)
        print(context['tracks'])
        return context

class ALbumLIst(ListView):
    model = Album
    template_name = 'base/list_pages/albums.html'
    context_object_name = 'albums'
    query_pk_and_slug = True
