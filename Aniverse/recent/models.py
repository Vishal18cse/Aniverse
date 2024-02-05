from django.db import models
from autoslug import AutoSlugField

class recently_updated(models.Model):
    name = models.CharField(max_length = 150)
    dis = models.CharField(max_length = 150)
    img = models.FileField(upload_to = 'recently_updated/' , max_length=250 , null=True , default=None)
    recent_slug = AutoSlugField(populate_from = 'name' , null=True , unique = True , default = None)
