from django.db import models
from django.urls import reverse
import datetime
from .category import Categorie

class Genre(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, primary_key=True)
    genre_categorie = models.ForeignKey('Categorie',blank=True, on_delete=models.CASCADE)
    
            
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("genre-detail", kwargs={"slug": self.slug})