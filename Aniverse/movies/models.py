from django.db import models
from autoslug import AutoSlugField

class anime_movies(models.Model):
    name = models.CharField(max_length = 250)
    dis = models.CharField(max_length=250)
    img = models.FileField(upload_to = 'anime_movies/' , max_length= 250, null = True ,default = None )
    movie_slug = AutoSlugField(populate_from = 'name' , unique = True , null = True , default = None)
    

