from django.db import models
from autoslug import AutoSlugField

class top_airing(models.Model):
    name = models.CharField(max_length = 150)
    dis = models.CharField(max_length = 150)
    img = models.FileField(upload_to = 'top_airing/' , max_length=250 , null=True , default=None)
    top_slug = AutoSlugField(populate_from = 'name' , unique = True , null = True , default = None)
