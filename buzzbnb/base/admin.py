from django.contrib import admin

from django.contrib import admin
from .models import Artist,Album,Song,GenreAndCategorie

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = 'name', 'known_as'

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
   date_hierarchy = 'release_date'
   list_display = 'title', 'artist', 'album', 'release_date'

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    date_hierarchy = 'release_date'
    list_display = 'title','artist', 'release_date'

@admin.register(GenreAndCategorie)
class GenreAdmin(admin.ModelAdmin):
    pass

