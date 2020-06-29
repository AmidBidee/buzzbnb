from django.db import models
from django.urls import reverse
import datetime
from .genre import Genre
from .category import Categorie

class Artist(models.Model):
    name = models.CharField(max_length=100)
    known_as = models.CharField(max_length=60)
    genre = models.ManyToManyField(Genre)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, blank=True)
    image = models.ImageField(upload_to='uploads/media/images/artist_image/%y/%m/%d')
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['known_as']
    
    def __str__(self):
        return self.known_as
    
    def get_absolute_url(self):
        return reverse("artist-detail", kwargs={"slug": self.slug, 'pk': self.pk})