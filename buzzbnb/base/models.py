from django.db import models
from django.urls import reverse

#class SongManager(models.Manager):
    #def get_queryset(self):
        #return super(SongManager,
                     #self).get_queryset()\
                          #.filter(songs='all_songs')
#class Single(models.Model):
    #return models.CharField()

class GenreAndCategorie(models.Model):
    name = models.CharField(max_length=30, blank=True)

    class Meta:
        ordering = ['-name']
    
    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=100)
    known_as = models.CharField(max_length=60)
    genre_or_categorie = models.ManyToManyField(GenreAndCategorie, related_name='genre_or_categorie')
    image = models.ImageField(upload_to='uploads/media/images/artist_image/%y/%m/%d')
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['-known_as']
    
    def __str__(self):
        return self.known_as
    
    def get_absolute_url(self):
        return reverse("artist-detail", kwargs={"slug": self.slug, 'pk': self.pk})
    
    

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

class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artist')
    featured_artist = models.ManyToManyField(Artist, blank=True)
    track_lenght = models.FloatField(blank=True)
    genre = models.ManyToManyField(GenreAndCategorie, related_name='genre')
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album')
    track_number = models.IntegerField(blank=True, null=True)
    release_date = models.DateField(auto_now_add=False, blank=True)
    image = models.ImageField(upload_to='uploads/media/images/song_image/%y/%m/%d')
    file = models.FileField(upload_to='uploads/media/files/song_files/%y/%m/%d')
    slug = models.SlugField(unique=True, default='')
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("song-detail", kwargs={"slug": self.slug, 'pk':self.pk})

    class Meta:
        ordering = ['-release_date']



