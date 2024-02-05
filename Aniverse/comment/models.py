from django.db import models
from store.models import storage
from django.contrib.auth.models import User

class Comment(models.Model):
    
    message = models.TextField()
    user = models.ForeignKey(User , on_delete = models.CASCADE)
    anime = models.ForeignKey(storage , on_delete = models.CASCADE)
    parent = models.ForeignKey('self' ,on_delete = models.CASCADE , null = True)
    created_at = models.DateTimeField(auto_now_add = True)
