from django.urls import path, re_path
from . import views
from .views import LatestSongs,HomePage,categorie_or_genre,ArtistList,AllCategories,AllGenres,SongsByCategorie,SongsByGenres

pr = ['all_songs','categorie_or_genre', 'categories', 'genres', 'song', 'all-artist', 'all-albums','album']

urlpatterns = [
    path('', LatestSongs, name='Home'),
    path('%s/%s/'%(pr[0], pr[1]), categorie_or_genre, name='categorie_or_genre'),
    path('%s/%s/%s/'%(pr[0], pr[1], pr[2]), AllCategories.as_view(), name='all-categories'),
    path('%s/%s/%s/'%(pr[0], pr[1], pr[3]), AllGenres.as_view(), name='all-genres'),
    path('%s/%s/<slug:slug>/'%(pr[0], pr[2]), SongsByCategorie.as_view(), name='categorie-detail'),
    path('%s/%s/<slug:slug>/'%(pr[0], pr[3]), SongsByGenres.as_view(), name='genre-detail'),
    path('%s/<int:pk>/<slug:slug>/'%(pr[4]), views.SongDetail.as_view(), name='song-detail'),
    path('all-artists/', ArtistList.as_view(), name='all-artists'),
    path("artist/<int:pk>/<slug:slug>/", views.ArtistDetail.as_view(), name="artist-detail"),
    path('all-albums/', views.ALbumLIst.as_view(), name='all-albums'),
    path('album/<int:pk>/<slug:slug>/', views.AlbumDetail.as_view(), name='album-detail'),

    #path('%s/%s/'%(pr[0], pr[1]), categorie_or_genre, name='categorie_or_genre'),
    #path('%s/%s/%s/'%(pr[0], pr[1], pr[2]), AllCategories.as_view(), name='all-categories'),
    #path('%s/%s/%s/'%(pr[0], pr[1], pr[3]), AllGenres.as_view(), name='all-genres'),
    #path('%s/%s/<slug:slug>/'%(pr[0], pr[2]), SongsByCategorie.as_view(), name='categorie-detail'),
    #path('%s/%s/<slug:slug>/'%(pr[0], pr[3]), SongsByGenres.as_view(), name='genre-detail'),
    #path('%s/<int:pk>/<slug:slug>/'%(pr[4]), views.SongDetail.as_view(), name='song-detail'),

 ]
