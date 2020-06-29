from django.contrib import admin

from django.contrib import admin
from .models import Artist, Album, Song, Genre, Categorie

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = 'name', 'known_as'
    prepopulated_fields = {'slug': ('known_as',)}

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
   date_hierarchy = 'release_date'
   list_display = 'title', 'artist', 'album', 'release_date'
   prepopulated_fields = {'slug': ('artist','title')}

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    date_hierarchy = 'release_date'
    list_display = 'title','artist', 'release_date'
    prepopulated_fields = {'slug': ('artist', 'title')}

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


