from django.db import models
from django.urls import reverse
import datetime

class Categorie(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, primary_key=True)

    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categorie-detail', kwargs={'slug': self.slug})