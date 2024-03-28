from django.db import models

# Create your models here.
   
class MovieReview(models.Model):
    username = models.CharField(max_length = 30)
    movieName = models.CharField(max_length = 50)
    rating = models.CharField(max_length = 2)
    review = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.username}{self.movieName}"
