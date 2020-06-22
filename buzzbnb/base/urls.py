from django.urls import path, re_path
from . import views
from .views import LatestSongs,HomePage,AllSongsList,ArtistList


urlpatterns = [
    path('', LatestSongs, name='Home'),
    path('all-songs/', AllSongsList.as_view(), name='all-songs'),
    path('song/<int:pk>/<slug:slug>/', views.SongDetail.as_view(), name='song-detail'),
    path('all-artists/', ArtistList.as_view(), name='all-artists'),
    path("artist/<int:pk>/<slug:slug>/", views.ArtistDetail.as_view(), name="artist-detail"),
    path('all-albums/', views.ALbumLIst.as_view(), name='all-albums'),
    path('album/<int:pk>/<slug:slug>/', views.AlbumDetail.as_view(), name='album-detail'),

 ]
