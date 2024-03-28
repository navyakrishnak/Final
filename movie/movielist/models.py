from django.db import models

class Movies(models.Model):
    name = models.CharField(max_length=30)
    poster = models.ImageField(blank=True, upload_to='moviepotser')
    desc = models.TextField(max_length=300)
    releaseDate = models.DateField()
    youtubelink = models.URLField()
    username = models.CharField(max_length=30)  # Assuming max_length as 30 for username
    actors = models.CharField(max_length=100)
    category = models.CharField(max_length=30)  # Assuming max_length as 30 for category

    def __str__(self):
        return self.name
    
