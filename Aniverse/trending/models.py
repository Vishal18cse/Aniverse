from django.db import models
from autoslug import AutoSlugField

class trending_anime(models.Model):
    name = models.CharField(max_length = 150)
    dis = models.CharField(max_length = 150)
    img = models.FileField(upload_to = 'trending/' , max_length=250 , null=True , default=None)
    trend_slug = AutoSlugField(populate_from = 'name' ,unique = True , null = True , default = None)


