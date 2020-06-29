
from django.db import models
from django.urls import reverse
import datetime
from .category import Categorie
from .genre import Genre
from .artist import Artist
from .album import Album


today = datetime.datetime.now()

class LatestSongManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(release_date__year=today.year)

class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artist')
    featured_artist = models.ManyToManyField(Artist, blank=True)
    track_lenght = models.FloatField(blank=True)
    genre = models.ManyToManyField(Genre)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album')
    track_number = models.IntegerField(blank=True, null=True)
    release_date = models.DateField(auto_now_add=False, blank=True)
    image = models.ImageField(upload_to='uploads/media/images/song_image/%y/%m/%d')
    file = models.FileField(upload_to='uploads/media/files/song_files/%y/%m/%d')
    slug = models.SlugField(unique=True, default='')
    objects = models.Manager()
    latest_songs = LatestSongManager()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("song-detail", kwargs={"slug": self.slug, 'pk':self.pk})

    class Meta:
        ordering = ['-release_date']