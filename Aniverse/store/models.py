from django.db import models
from autoslug import AutoSlugField
from django.contrib.auth.models import User

class storage(models.Model):
    name = models.CharField(max_length = 250)
    dis = models.CharField(max_length = 125)
    img = models.FileField(upload_to='anime_store/' , max_length= 250 , null = True , default = None)
    slug = AutoSlugField(populate_from = 'name' , unique = True , null = True , default = None)
    i_img = models.FileField(upload_to='img/' , max_length= 250 , null = True , default = None)
    story = models.TextField(null=True , default=None)
    i1 = models.FileField(upload_to='screenshot/' , max_length= 250 , null = True , default = None)
    i2 = models.FileField(upload_to='screenshot/' , max_length= 250 , null = True , default = None)
    i3 = models.FileField(upload_to='screenshot/' , max_length= 250 , null = True , default = None)
    i4 = models.FileField(upload_to='screenshot/' , max_length= 250 , null = True , default = None)

    def __str__(self):
        return self.name



class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(storage)

    def __str__(self):
        return f"Wishlist for {self.user.username}"



class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(storage)  # Replace 'YourProductModel' with the actual model representing your products

    def __str__(self):
        return f'Favorites for {self.user.username}'

