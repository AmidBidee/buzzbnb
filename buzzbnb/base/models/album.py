from django.db import models
from django.urls import reverse
import datetime
from .artist import Artist

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    release_date = models.DateField(blank=True, null=True)
    number_of_tracks = models.IntegerField()
    album_art = models.ImageField(upload_to='uploads/media/images/album_arts/%y/%m/%d')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("album-detail", kwargs={"slug": self.slug, 'pk': self.pk})

    class Meta:
        ordering = ['-release_date']
