from django.db import models

class a_anime(models.Model):
    name = models.CharField(max_length=50)
    dis = models.TextField(null=True , default=None)
    img = models.FileField(upload_to="anime/" ,max_length=250 , null=True , default=None)

class b_anime(models.Model):
    name = models.CharField(max_length=50)
    dis = models.TextField(null=True , default=None)
    img = models.FileField(upload_to="anime/" ,max_length=250 , null=True , default=None)

class c_anime(models.Model):
    name = models.CharField(max_length=50)
    dis = models.TextField(null=True , default=None)
    img = models.FileField(upload_to="anime/" ,max_length=250 , null=True , default=None)    